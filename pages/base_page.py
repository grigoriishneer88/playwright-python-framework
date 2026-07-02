from re import Pattern
import allure
from playwright.sync_api import Page, expect

from tools.logger import get_logger, logger


class BasePage:
    logger = get_logger("BasePage")

    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        step = f'Opening URL {url}'
        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until="load")

    def reload(self):
        step = f'Reloading {self.page}'
        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until="load")

    def check_if_visible(self, element):
        expect(element).to_be_visible()

    def check_text(self, element, text):
        expect(element).to_have_text(text)

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that current URL matches the URL {expected_url.pattern}'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
