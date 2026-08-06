import allure
import os
import pytest
from playwright.sync_api import sync_playwright, Page, Playwright

from config import settings
from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest

from tools.playwright.pages import initialize_playwright_page


@pytest.fixture(params=settings.browser)
def page(request: SubRequest, playwright:Playwright):
    yield from initialize_playwright_page(playwright, test_name = request.node.name, storage_stage = None, browser_type=request.param)


@pytest.fixture(scope="session")  # Просто сессионный scope, без autouse
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    try:
        page = context.new_page()
        registration_page = RegistrationPage(page=page)
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form_component.fill_form(
            email=settings.test_user.email,
            password=settings.test_user.password,
            name=settings.test_user.username
        )
        registration_page.click_registration_button()
        context.storage_state(path=settings.browser_state_file)
    finally:
        context.close()
        browser.close()

@pytest.fixture(params=settings.browser)
def page_with_state(request: SubRequest, playwright:Playwright):
    yield from initialize_playwright_page(playwright, test_name = request.node.name, storage_stage = settings.browser_state_file, browser_type=request.param)

