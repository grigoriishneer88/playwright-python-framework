import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.courses.courses_list_page import CoursesPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.parent_suites import AllureParentSuite
from tools.allure.stories import AllureStories
from tools.allure.sub_suite import AllureSubSuite
from tools.allure.suites import AllureSuite
from tools.allure.tags import AllureTags


@pytest.mark.courses
@allure.epic(AllureEpic.LMS.value)
@allure.feature(AllureFeature.COURSES.value)
@allure.story(AllureStories.COURSES.value)
@allure.parent_suite(AllureParentSuite.LMS.value)
@allure.suite(AllureSuite.COURSES.value)
@allure.sub_suite(AllureSubSuite.COURSES.value)
class TestCreateCourseExercises:

    @pytest.mark.xfail(reason="Known issue: exercise can be created with empty title")
    @allure.severity(Severity.CRITICAL)
    @allure.title("Try to create course with exercises without exercise title")
    @allure.tag(AllureTags.COURSES.value)
    def test_add_course_with_exercise_without_exercise_title(self, create_course_page: CreateCoursePage, courses_list_page: CoursesPage):
        create_course_page.visit_create_course_page()
        create_course_page.create_course_form_component.check_visible()
        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.check_exercises_empty_view_visibility()
        create_course_page.create_course_form_component.fill(
            'course with exercise',
            '12',
            'course with exercise description',
            '11',
            '2'
        )
        create_course_page.create_course_exercises_toolbar_view_component.create_new_exercise_button.click()
        create_course_page.create_course_exercise_form.fill_create_exercise_form(0, None,
                                                                                 'exercise 1 just without title')
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=False)
        create_course_page.upload_image_widget.upload_preview_image(
            settings.test_data.image_png_file)
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_toolbar_view_component.check_visible(is_create_course_disabled=True)


    @pytest.mark.xfail(reason="Known issue: exercise can be created with empty description")
    @allure.severity(Severity.CRITICAL)
    @allure.title("Try to create course with exercises without exercise description")
    @allure.tag(AllureTags.COURSES.value)
    def test_add_course_with_exercise_without_exercise_description(self, create_course_page: CreateCoursePage,
                                                             courses_list_page: CoursesPage):
        create_course_page.visit_create_course_page()
        create_course_page.create_course_form_component.check_visible()
        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.check_exercises_empty_view_visibility()
        create_course_page.create_course_form_component.fill(
            'course with exercise',
            '12',
            'course with exercise description',
            '11',
            '2'
        )
        create_course_page.create_course_exercises_toolbar_view_component.create_new_exercise_button.click()
        create_course_page.create_course_exercise_form.fill_create_exercise_form(0, "exercise 1 just without description",
                                                                                None)
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=False)
        create_course_page.upload_image_widget.upload_preview_image(
            settings.test_data.image_png_file)
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_toolbar_view_component.check_visible(is_create_course_disabled=True)


