# import pytest
# from playwright.sync_api import sync_playwright, Page, Playwright
#
#
# @pytest.fixture
# def chromium_page(playwright) -> Page:
#     browser = playwright.chromium.launch(headless=False)
#     page = browser.new_page()
#     yield page
#     browser.close()
#
# @pytest.fixture(scope="session")
# def initialize_browser_state(playwright) -> Page:
#     brw = playwright.chromium.launch(headless=False)
#     context = brw.new_context()
#     page = context.new_page()
#     page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
#     email_field = page.get_by_test_id("registration-form-email-input").locator('input')
#     name_field = page.get_by_test_id("registration-form-username-input").locator('input')
#     password_field = page.get_by_test_id("registration-form-password-input").locator('input')
#     registration_button = page.get_by_test_id("registration-page-registration-button")
#     email_field.fill("test2@test.com")
#     name_field.fill("test2")
#     password_field.fill("test2")
#     registration_button.click()
#     context.storage_state(path = 'storageState.json')
# @pytest.fixture
# def chromium_page_with_state(playwright) -> Page:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context(storage_state='storageState.json')
#     page = context.new_page()
#     yield page
#     browser.close()
