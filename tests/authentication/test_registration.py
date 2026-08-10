import allure
import pytest
from playwright.sync_api import Page
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.parent_suites import AllureParentSuite
from tools.allure.sub_suite import AllureSubSuite
from tools.allure.suites import AllureSuite
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeature
from allure_commons.types import Severity

@pytest.mark.regression
@pytest.mark.registration
@allure.epic(AllureEpic.LMS.value)
@allure.parent_suite(AllureParentSuite.LMS.value)
@allure.feature(AllureFeature.AUTHENTICATION.value)
@allure.suite(AllureSuite.AUTHENTICATION.value)
@allure.story(AllureStories.REGISTRATION.value)
@allure.sub_suite(AllureSubSuite.REGISTRATION.value)
class TestRegistration:
    @pytest.mark.parametrize(
        "email, password, username",  # 1. Имена переменных одной строкой через запятую
        [
            ("test2@test.com", "test2", "test2")
        ]
    )
    @pytest.mark.regression
    @pytest.mark.registration
    @pytest.mark.already_signed_in
    @allure.title("Register with email and password")
    @allure.tag(AllureTags.REGISTRATION.value, AllureTags.REGISTRATION.value)
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.xdist_group(name='authorisation-group')
    def test_successful_registration(self, page: Page, dashboard_page: DashboardPage, registration_page: RegistrationPage, email:str, username:str, password:str):
            registration_page.visit_registration_page()
            registration_page.registration_form_component.fill_form(email, username, password)
            registration_page.click_registration_button()
            dashboard_page.dashboard_toolbar_view_component.check_visible()
            dashboard_page.side_bar_component.check_visible()
            dashboard_page.side_bar_component.click_logout()

