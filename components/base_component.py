from playwright.sync_api import Page, expect
from re import Pattern
from tools.logger import get_logger


class BaseComponent:
    logger = get_logger("BaseComponent")

    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        self.logger.info(f'Checking current url: {expected_url}')
        expect(self.page).to_have_url(expected_url)
