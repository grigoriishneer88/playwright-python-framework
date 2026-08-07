from re import Pattern
import allure
from playwright.sync_api import Page, expect, Locator

from tools.logger import get_logger


class BasePage:
    logger = get_logger("BasePage")

    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        step = f'Opening URL {url}'
        with allure.step(step):
            self.logger.info(step)
            self.page.goto(url, wait_until="domcontentloaded")
        return self

    def reload(self):
        step = f'Reloading {self.page}'
        with allure.step(step):
            self.logger.info(step)
            self.page.reload(wait_until="domcontentloaded")

    def check_if_visible(self, element: Locator):
        expect(element).to_be_visible()

    def check_text(self, element: Locator, text: str):
        expect(element).to_have_text(text)

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that current URL matches the URL {expected_url.pattern}'
        with allure.step(step):
            self.logger.info(step)
            expect(self.page).to_have_url(expected_url)
