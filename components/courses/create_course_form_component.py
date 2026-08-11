from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.input import Input
from elements.textarea import TextArea
#updated import


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)
        # create course form
        self.create_course_title_input = Input(page, 'create-course-form-title-input', 'Create Course Title')
        self.create_course_estimated_time_input = Input(page,
            'create-course-form-estimated-time-input',
            'Create Course Estimated Time')
        self.create_course_description_input = TextArea(page, 'create-course-form-description-input', 'Create Course Description')
        self.create_course_max_score_input = Input(page, 'create-course-form-max-score-input', 'Create Course Max Score')
        self.create_course_min_score_input = Input(page, 'create-course-form-min-score-input', 'Create Course Min Score')

    def check_visible(self):
        self.create_course_title_input.check_visible()
        self.create_course_estimated_time_input.check_visible()
        self.create_course_description_input.check_visible()
        self.create_course_max_score_input.check_visible()
        self.create_course_min_score_input.check_visible()

    def fill(self, title : str | None, estimated: str | None, description: str | None, max_score: str | None, min_score: str | None):
        if title is not None:
            self.create_course_title_input.fill(title)
            self.create_course_title_input.check_have_value(title)
        if estimated is not None:
            self.create_course_estimated_time_input.fill(estimated)
            self.create_course_estimated_time_input.check_have_value(estimated)
        if description is not None:
            self.create_course_description_input.fill(description)
            self.create_course_description_input.check_have_value(description)
        if max_score is not None:
            self.create_course_max_score_input.fill(max_score)
            self.create_course_max_score_input.check_have_value(max_score)
        if min_score is not None:
            self.create_course_min_score_input.fill(min_score)
            self.create_course_min_score_input.check_have_value(min_score)

    def check_filled_fields_on_edit_or_add_course_page(self, title : str | None, estimated: str | None, description: str | None, max_score: str | None, min_score: str | None):
        if title is not None:
            self.create_course_title_input.check_have_value(title)
        if estimated is not None:
            self.create_course_estimated_time_input.check_have_value(estimated)
        if description is not None:
            self.create_course_description_input.check_have_value(description)
        if max_score is not None:
            self.create_course_max_score_input.check_have_value(max_score)
        if min_score is not None:
            self.create_course_min_score_input.check_have_value(min_score)