from playwright.sync_api import Page

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage
from tools.routes import AppRoute


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.create_course_toolbar_view_component = CreateCourseToolbarViewComponent(page)
        self.create_course_form_component = CreateCourseFormComponent(page)
        self.preview_empty_view = EmptyViewComponent(page,'create-course-preview')
        self.upload_image_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.create_course_exercise_form = CreateCourseExerciseFormComponent(page)
        self.create_course_exercises_toolbar_view_component = CreateCourseExercisesToolbarViewComponent(page)

        #exercises area
        #empty exercises aria
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')

    def visit_create_course_page(self):
        self.visit(AppRoute.CREATE_COURSE)

    def check_preview_empty_view_visibility(self):
        self.preview_empty_view.check_visible(title='No image selected', description='Preview of selected image will be displayed here')

    def check_exercises_empty_view_visibility(self):
        self.exercises_empty_view.check_visible(title='There is no exercises', description='Click on "Create exercise" button to create new exercise')

    # def get_exercise_index_by_name(self, title: str):
    #     exercise_names = self.exercises_title.all()
    #     exercise_index = None
    #     for index, exercise_name in exercise_names:
    #         exercise_name_text = exercise_name.text_content()
    #         if title == exercise_name_text:
    #             exercise_index = index
    #     return exercise_index
