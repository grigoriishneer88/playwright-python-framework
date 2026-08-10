import allure

from components.authentication.login_form_component import LoginFormComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page
import re

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_form_component = LoginFormComponent(page)
        self.login_button = Button(page, 'login-page-login-button', 'Login')
        self.register_link = Link(page, 'login-page-registration-link', 'Registration')
        self.wrong_email_or_password_alert = Text(page,'login-page-wrong-email-or-password-alert', 'Wrong Email or Password')

    def click_login_button(self):
        self.login_button.click()

    def click_register_link(self):
        self.register_link.click()
        self.check_current_url(re.compile('.*/#/auth/registration'))

    @allure.step('Check Wrong email alert is visible')
    def check_wrong_email_or_password_alert(self):
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text("Wrong email or password")

    @allure.step('Check Login button is visible')
    def check_login_button_is_visible(self):
        self.login_button.check_visible()