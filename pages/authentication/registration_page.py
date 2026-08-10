import re

from playwright.sync_api import Page

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage
from tools.routes import AppRoute


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form_component = RegistrationFormComponent(page)
        self.registration_button = Button(page,"registration-page-registration-button", 'registration-page-registration-button')
        self.login_link = Link(page,"registration-page-login-link", 'Login link')


    def click_registration_button(self):
        self.registration_button.click()

    def visit_registration_page(self):
        self.visit(AppRoute.REGISTRATION)

    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile(AppRoute.LOGIN))

    def check_registration_button_is_disabled(self):
        self.registration_button.check_disabled()