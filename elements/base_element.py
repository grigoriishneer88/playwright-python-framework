import allure
from playwright.sync_api import Page, expect, Locator
from ui_coverage_tool import ActionType, SelectorType

from elements.ui_coverage import tracker
from tools.logger import get_logger


class BaseElement:
    logger = get_logger('Base_Element')

    def __init__(self, page:Page, locator:str, name:str):
        self.page = page
        self.name = name
        self.locator = locator

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        step = f'Getting locator with "data-testid={locator}" at index" {nth}"'
        with allure.step(step):
            self.logger.info(step)
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self,nth:int = 0,**kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Clicking {self.type_of} with name {self.name} and "data-testid={locator}" at index" {nth}"'
        with allure.step(step):
            self.logger.info(step)
            locator.click()

        self.track_coverage(ActionType.CLICK, nth, **kwargs)

    def check_visible(self, nth:int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking {self.type_of} with name {self.name} is VISIBLE and "data-testid={locator}" at index" {nth}"'
        with allure.step(step):
            self.logger.info(step)
            expect(locator).to_be_visible()
        self.track_coverage(ActionType.VISIBLE, nth, **kwargs)

##added just now
    def check_not_visible(self, nth:int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking {self.type_of} with name {self.name} is NOT VISIBLE and "data-testid={locator}" at index" {nth}"'
        with allure.step(step):
            self.logger.info(step)
            expect(locator).to_be_hidden()
        self.track_coverage(ActionType.HIDDEN, nth, **kwargs)

    def check_not_have_text(self, text:str,nth:int = 0,**kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking that {self.type_of} with name {self.name} has NO text {text} and "data-testid={locator}" at index" {nth}"'
        with allure.step(step):
            self.logger.info(step)
            expect(locator).not_to_have_text(text)

        self.track_coverage(ActionType.TEXT, nth, **kwargs)

    def check_have_text(self, text:str,nth:int = 0,**kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking that {self.type_of} with name {self.name} has text {text} and "data-testid={locator}" at index" {nth}"'
        with allure.step(step):
            self.logger.info(step)
            expect(locator).to_have_text(text)

        self.track_coverage(ActionType.TEXT, nth, **kwargs)

    def track_coverage(self, action_type:ActionType,nth:int = 0,**kwargs):
        tracker.track_coverage(
            selector=self.get_row_locator(nth, **kwargs),
            action_type=action_type,
            selector_type=SelectorType.XPATH
        )


    @property
    def type_of(self):
        return "base element"

    def get_row_locator(self, nth:int = 0, **kwargs):
        return f"//*[@data-testid='{self.locator.format(**kwargs)}'][{nth+1}]"
