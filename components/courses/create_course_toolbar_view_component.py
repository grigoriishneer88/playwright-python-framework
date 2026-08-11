from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = Text(page, 'create-course-toolbar-title-text', 'Create Course Toolbar Title')
        self.button = Button(page, 'create-course-toolbar-create-course-button', 'Create Course Toolbar Button')

    def click_create_course_button(self):
        self.button.click()

    def check_visible(self, is_create_course_disabled=True):
        self.button.check_visible()
        if is_create_course_disabled:
            self.button.check_disabled()
        else:
            self.button.check_enabled()

