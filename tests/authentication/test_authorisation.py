from allure_commons.types import Severity
from playwright.sync_api import Page
import pytest
import allure

from config import settings
from fixtures.pages import login_page
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.login_page import LoginPage
from tools.allure.parent_suites import AllureParentSuite
from tools.allure.sub_suite import AllureSubSuite
from tools.allure.suites import AllureSuite
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeature

@pytest.mark.xdist_group(name='authorisation-group')
@allure.parent_suite(AllureParentSuite.LMS.value)
@allure.suite(AllureSuite.AUTHENTICATION.value)
@allure.sub_suite(AllureSubSuite.AUTHORISATION.value)
@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.already_signed_in
@allure.tag(AllureTags.REGRESSION.value, AllureTags.AUTHORISATION.value)
@allure.epic(AllureEpic.LMS.value)
@allure.feature(AllureFeature.AUTHENTICATION.value)
@allure.story(AllureStories.AUTHORISATION.value)
class TestAuthorisation:
    @pytest.mark.xdist_group(name='authorisation-group')
    @pytest.mark.regression
    @pytest.mark.authorisation
    @pytest.mark.parametrize('email, password', [
        ('email1', 'password'),
        ('email2', 'password1'),
        ('email3', 'password2'),
        ('email4', 'password3'),
    ])
    @allure.tag(AllureTags.USER_LOGIN.value)
    @allure.title("Testing authorisation with wrong email or wrong password")
    @allure.severity(Severity.CRITICAL.value)
    def test_wrong_email_or_password(self, login_page: LoginPage, email: str, password: str):
        # allure.dynamic.title(f"Testing authorisation with wrong email:{email} or wrong password : {password}")
        login_page.visit("./#/auth/login")
        login_page.login_form_component.fill(email, password)
        login_page.login_form_component.check_visible(email, password)
        login_page.click_login_button()
        login_page.check_wrong_email_or_password_alert()

    @allure.title("Dashboard available after authorisation with proper email and password")
    @pytest.mark.already_signed_in
    def test_sign_in(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit("./#/dashboard")
        dashboard_page_with_state.dashboard_toolbar_view_component.check_visible()

    @allure.severity(Severity.BLOCKER.value)
    @allure.tag(AllureTags.USER_LOGIN.value)
    @allure.title("Testing authorisation with proper email and password")
    def test_successful_authorization(self, login_page: LoginPage, dashboard_page: DashboardPage, registration_page: RegistrationPage):
        registration_page.visit_registration_page()
        registration_page.registration_form_component.fill_form(email = settings.test_user.email, username=settings.test_user.username, password=settings.test_user.password)
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar_component.check_nav_bar_visibility(settings.test_user.username)
        dashboard_page.side_bar_component.check_visible()
        dashboard_page.side_bar_component.click_logout()
        login_page.login_form_component.fill(email = settings.test_user.email, password=settings.test_user.password)
        login_page.click_login_button()
        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar_component.check_nav_bar_visibility(settings.test_user.username)


    @allure.title("Navigation from Login page to Registration page")
    @allure.tag(AllureTags.NAVIGATION.value)
    @allure.severity(Severity.NORMAL.value)
    def test_navigate_from_authorisation_to_registration_page(self, login_page: LoginPage, registration_page: RegistrationPage):
        login_page.visit("./#/auth/login")
        login_page.click_register_link()
        registration_page.registration_form_component.check_visible()

    @allure.title("User is returned to Login page after logout")
    @allure.tag(AllureTags.AUTHORISATION.value)
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.already_signed_in
    def test_logout(
            self,
            dashboard_page_with_state: DashboardPage,
    ):
        dashboard_page_with_state.visit_dashboard_page()
        dashboard_page_with_state.side_bar_component.click_logout()
        login_page_after_logout = LoginPage(dashboard_page_with_state.page)
        login_page_after_logout.check_login_button_is_visible()
