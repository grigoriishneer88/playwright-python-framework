import allure
from playwright.sync_api import expect
from ui_coverage_tool import ActionType
from elements.base_element import BaseElement
from tools.logger import get_logger


class TextArea(BaseElement):
    logger = get_logger("TextArea")

    @property
    def type_of(self):
        return "textarea"

    def get_locator(self,nth:int = 0,  **kwargs):
        return super().get_locator(nth, **kwargs).locator('textarea').first

    def fill(self, value:str,nth:int = 0,  **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Fill {self.type_of} with name {self.name} by {value} and "data-testid={locator}" at index" {nth}"'
        with allure.step(step):
            self.logger.info(step)
            locator.fill(value)
        self.track_coverage(ActionType.FILL, nth, **kwargs)


    def check_have_value(self, value:str,nth:int = 0,  **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step =f'Check that {self.type_of} with name {self.name} has value: {value}, and "data-testid={locator}" at index" {nth}"'
        with allure.step(step):
            self.logger.info(step)
            expect(locator).to_have_value(value)
        self.track_coverage(ActionType.VALUE, nth, **kwargs)

