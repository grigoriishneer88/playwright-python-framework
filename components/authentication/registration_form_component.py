import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_field = Input(page, "registration-form-email-input", 'email')
        self.name_field = Input(page, "registration-form-username-input", 'name')
        self.password_field = Input(page,"registration-form-password-input", 'password')

    @allure.step("Fill registration form")
    def fill_form(self, email: str, username: str, password: str):
        self.email_field.fill(email)
        self.name_field.fill(username)
        self.password_field.fill(password)

    @allure.step("Check that registration form is visible")
    def check_visible(self):
        self.email_field.check_visible()
        self.name_field.check_visible()
        self.password_field.check_visible()