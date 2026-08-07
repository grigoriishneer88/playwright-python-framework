import allure
from playwright.sync_api import expect
from ui_coverage_tool import ActionType

from elements.base_element import BaseElement
from tools.logger import get_logger


class Button(BaseElement):
    logger = get_logger('Button')

    @property
    def type_of(self):
        return "button"

    def check_enabled(self, nth:int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking that {self.type_of} with name {self.name} is ENABLED and "data-testid={locator}" at index" {nth}"'
        with allure.step(step):
            self.logger.info(step)
            expect(locator).to_be_enabled()
        self.track_coverage(ActionType.ENABLED, nth, **kwargs)

    def check_disabled(self,nth:int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking that {self.type_of} with name {self.name} is DISABLED and "data-testid={locator}" at index" {nth}"'
        with allure.step(step):
            self.logger.info(step)
            expect(locator).to_be_disabled()
        self.track_coverage(ActionType.DISABLED, nth, **kwargs)


    def check_hidden(self, nth:int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking that {self.type_of} with name {self.name} is HIDDEN and "data-testid={locator}" at index" {nth}"'
        with allure.step(step):
            self.logger.info(step)
            expect(locator).to_be_hidden()
        self.track_coverage(ActionType.HIDDEN, nth, **kwargs)
