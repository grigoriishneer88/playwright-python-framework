import allure

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.button import Button

class CourseMenuViewComponent(BaseComponent):
    def __init__(self,page: Page):
        super().__init__(page)
        self.menu_button = Button(page,'course-view-menu-button', 'Menu')
        self.edit_button = Button(page, 'course-view-edit-menu-item-icon', 'Edit')
        self.delete_button = Button(page, 'course-view-delete-menu-item-text', 'Delete')
        self.modal_confirm_button = Button(page, 'modal-confirm-button', 'Delete')

    @allure.step('Open Course menu at "{index}" and click Edit')
    def click_edit(self, index:int):
        self.menu_button.click(nth=index)
        self.edit_button.check_visible(nth=index)
        self.edit_button.click(nth=index)

    @allure.step('Open Course menu at "{index}" and click Delete')
    def click_delete(self, index:int):
        self.menu_button.click(nth=index)
        self.delete_button.check_visible(nth=index)
        self.delete_button.click(nth=index)