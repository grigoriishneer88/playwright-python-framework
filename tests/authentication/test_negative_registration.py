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

class TestNegativeRegistration:
    @pytest.mark.parametrize(
        "email, username, password",
        [
            ("", "test_user", "test_password"),
            ("test@test.com", "", "test_password"),
            ("test@test.com", "test_user", ""),
        ],
        ids=[
            "empty_email",
            "empty_username",
            "empty_password",
        ],
    )
    @pytest.mark.registration
    @allure.title("Registration is unavailable when a required field is empty")
    @allure.tag(AllureTags.REGISTRATION.value)
    @allure.severity(Severity.NORMAL)
    def test_registration_button_is_disabled_with_empty_required_field(
        self,
        page: Page,
        registration_page: RegistrationPage,
        email: str,
        username: str,
        password: str,
    ):
        registration_page.visit_registration_page()
        registration_page.registration_form_component.fill_form(
            email, username, password
        )
        registration_page.check_registration_button_is_disabled()
