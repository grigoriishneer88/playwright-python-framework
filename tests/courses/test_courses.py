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
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.courses
@allure.epic(AllureEpic.LMS.value)
@allure.feature(AllureFeature.COURSES.value)
@allure.story(AllureStories.COURSES.value)
@allure.parent_suite(AllureParentSuite.LMS.value)
@allure.suite(AllureSuite.COURSES.value)
@allure.sub_suite(AllureSubSuite.COURSES.value)
class TestCourses:
    @allure.severity(Severity.CRITICAL)
    @allure.title("Create new course")
    @allure.tag(AllureTags.COURSES.value, AllureTags.REGRESSION.value)
    def test_add_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesPage):
        create_course_page.visit_create_course_page()
        create_course_page.create_course_form_component.check_visible()
        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.check_exercises_empty_view_visibility()
        create_course_page.create_course_form_component.fill(
            'course1',
            '12',
            'course 1 description',
            '11',
            '2'
        )
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=False)

        create_course_page.upload_image_widget.upload_preview_image(
            settings.test_data.image_png_file)
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_toolbar_view_component.click_create_course_button()
        courses_list_page.toolbar_view_component.check_create_course_button_visibility()
        courses_list_page.toolbar_view_component.check_courses_title_visibility()
        courses_list_page.course_view.check_visible(
            0,
            'course1',
            11,
            2,
            12,
        )

    @allure.severity(Severity.NORMAL)
    @allure.title("Check empty courses list")
    @allure.tag(AllureTags.COURSES.value, AllureTags.REGRESSION.value)
    def test_empty_course_list(self, courses_list_page: CoursesPage):
        courses_list_page.visit(AppRoute.COURSES)
        courses_list_page.navbar_component.check_nav_bar_visibility('test2')
        courses_list_page.check_empty_view_visibility()
        courses_list_page.empty_view.check_visible('There is no results',
                                                   'Results from the load test pipeline will be displayed here')
        courses_list_page.toolbar_view_component.check_courses_title_visibility()
        courses_list_page.toolbar_view_component.check_create_course_button_visibility()

    @allure.severity(Severity.CRITICAL)
    @allure.title("Change existing course")
    @allure.tag(AllureTags.COURSES.value, AllureTags.REGRESSION.value)
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesPage):
        create_course_page.visit_create_course_page()
        create_course_page.check_exercises_empty_view_visibility()
        course_title = 'test course'
        course_estimated = '12'
        course_description = 'just test'
        course_max_score = '89'
        course_min_score = '56'
        create_course_page.create_course_form_component.fill(title = course_title, estimated = course_estimated, description = course_description, max_score = course_max_score, min_score = course_min_score)
        create_course_page.upload_image_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.create_course_toolbar_view_component.click_create_course_button()
        courses_list_page.course_view.check_visible(index= 0, title = course_title, max_score = course_max_score, min_score=course_min_score, estimated_time=course_estimated)
        courses_list_page.course_view.menu.click_edit(index=0)
        course_title = 'test course changed'
        course_estimated = '16'
        course_description = 'just test changed'
        course_max_score = '100'
        course_min_score = '12'
        create_course_page.create_course_form_component.fill(title = course_title, estimated = course_estimated, description = course_description, max_score = course_max_score, min_score = course_min_score)
        create_course_page.create_course_toolbar_view_component.click_create_course_button()
        courses_list_page.course_view.check_visible(index= 0, title = course_title, max_score = course_max_score, min_score=course_min_score, estimated_time=course_estimated)

    @allure.severity(Severity.CRITICAL)
    @allure.title("Delete existing course")
    @allure.tag(AllureTags.COURSES.value, AllureTags.REGRESSION.value)
    def test_delete_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesPage):
        create_course_page.visit_create_course_page()
        create_course_page.create_course_form_component.check_visible()
        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.check_exercises_empty_view_visibility()
        create_course_page.create_course_form_component.fill(
            'delete',
            '12',
            'course 1 description',
            '11',
            '2'
        )
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=False)
        create_course_page.upload_image_widget.upload_preview_image(
            settings.test_data.image_png_file)
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_toolbar_view_component.click_create_course_button()
        courses_list_page.course_view.menu.click_delete(index=0)
        courses_list_page.course_view.menu.modal_confirm_button.click()
        courses_list_page.course_view.check_not_visible(0, 'delete')
        courses_list_page.check_empty_view_visibility()

    @allure.severity(Severity.CRITICAL)
    @allure.title("Try to create course with exercises")
    @allure.tag(AllureTags.COURSES.value, AllureTags.REGRESSION.value)
    def test_add_course_with_exercise(self, create_course_page: CreateCoursePage, courses_list_page: CoursesPage):
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
        create_course_page.create_course_exercise_form.fill_create_exercise_form(0, 'exercise 1 just try title',
                                                                                 'exercise 1 just try description')
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=False)
        create_course_page.upload_image_widget.upload_preview_image(
            settings.test_data.image_png_file)
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_toolbar_view_component.click_create_course_button()
        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.create_course_exercise_form.check_filled_create_exercise_form(0, 'exercise 1 just try title',
                                                                                         'exercise 1 just try description')
