import allure

from elements.base_element import BaseElement
from tools.logger import get_logger


class FileInput(BaseElement):
    logger = get_logger("FileInput")
    def type_of(self):
        return 'file input'

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        step = f'Set input file "{file}" to "{self.type_of} with name "{self.name}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            self.logger.info(step)
            locator.set_input_files(file)