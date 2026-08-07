from playwright.sync_api import Page
from playwright.sync_api import expect

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.button import Button
from elements.file_input import FileInput
from elements.icon import Icon
from elements.text import Text


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, ):    #'create-course-preview - identifier
        super().__init__(page)
        self.preview_empty_view = EmptyViewComponent(page,'create-course-preview')
        # upload image section
        self.image_upload_info_icon = Icon(page, f'{identifier}-image-upload-widget-info-icon', 'upload-image-upload-info-icon')
        self.image_upload_info_title = Text(page, f'{identifier}-image-upload-widget-info-title-text', 'upload_info_title')
        self.image_upload_info_description = Text(page,f'{identifier}-image-upload-widget-info-description-text', 'upload_info_description')
        self.upload_button = Button(page, f'{identifier}-image-upload-widget-upload-button', 'upload button')
        self.upload_input_file = FileInput(page, f'{identifier}-image-upload-widget-input', 'upload_input_file')

        # full view
        # image section
        self.preview_image = page.get_by_test_id(f'{identifier}-image-upload-widget-preview-image')

        # upload image section
        self.delete_image = page.get_by_test_id(f'{identifier}-image-upload-widget-remove-button')

    def check_visible(self, is_image_uploaded: bool = False):
        self.image_upload_info_icon.check_visible()
        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_have_text('Tap on "Upload image" button to select file')
        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text('Recommended file size 540X300')
        self.upload_button.check_visible()
        if is_image_uploaded:
            expect(self.delete_image).to_be_visible()
        else:
            expect(self.delete_image).to_be_hidden()

    def click_delete_image_button(self):
        self.delete_image.click()

    def upload_preview_image(self, file: str):
        self.upload_input_file.set_input_files(file)

