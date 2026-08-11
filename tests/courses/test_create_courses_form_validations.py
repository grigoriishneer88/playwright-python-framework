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


@pytest.mark.regression
@pytest.mark.courses
@allure.epic(AllureEpic.LMS.value)
@allure.feature(AllureFeature.COURSES.value)
@allure.story(AllureStories.COURSES.value)
@allure.parent_suite(AllureParentSuite.LMS.value)
@allure.suite(AllureSuite.COURSES.value)
@allure.sub_suite(AllureSubSuite.COURSES.value)


class TestCreateCoursesFormValidations:

    @allure.severity(Severity.CRITICAL)
    @allure.title("Try to create course with empty title")
    @allure.tag(AllureTags.COURSES.value, AllureTags.REGRESSION.value)
    def test_add_course_with_empty_title(self, create_course_page: CreateCoursePage, courses_list_page: CoursesPage):
        create_course_page.visit_create_course_page()
        create_course_page.create_course_form_component.check_visible()
        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.check_exercises_empty_view_visibility()
        create_course_page.upload_image_widget.upload_preview_image(
            settings.test_data.image_png_file)
        create_course_page.create_course_form_component.fill(None, "12", "course 1 description", "11", "2")
        create_course_page.create_course_toolbar_view_component.button.check_disabled()

    @allure.severity(Severity.CRITICAL)
    @allure.title("Try to create course with empty estimated time")
    @allure.tag(AllureTags.COURSES.value, AllureTags.REGRESSION.value)
    def test_add_course_with_empty_estimated_time(self, create_course_page: CreateCoursePage,
                                                  courses_list_page: CoursesPage):
        create_course_page.visit_create_course_page()
        create_course_page.create_course_form_component.check_visible()
        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.check_exercises_empty_view_visibility()
        create_course_page.upload_image_widget.upload_preview_image(
            settings.test_data.image_png_file)
        create_course_page.create_course_form_component.fill("no estimated time", None, "course 1 description", "11",
                                                             "2")
        create_course_page.create_course_toolbar_view_component.button.check_disabled()

    @allure.severity(Severity.CRITICAL)
    @allure.title("Try to create course with empty description")
    @allure.tag(AllureTags.COURSES.value, AllureTags.REGRESSION.value)
    def test_add_course_with_empty_description(self, create_course_page: CreateCoursePage,
                                               courses_list_page: CoursesPage):
        create_course_page.visit_create_course_page()
        create_course_page.create_course_form_component.check_visible()
        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.check_exercises_empty_view_visibility()
        create_course_page.upload_image_widget.upload_preview_image(
            settings.test_data.image_png_file)
        create_course_page.create_course_form_component.fill("no estimated time", "12", None, "11", "2")
        create_course_page.create_course_toolbar_view_component.button.check_disabled()

    @allure.severity(Severity.CRITICAL)
    @allure.title("Try to create course with 0 max score")
    @allure.tag(AllureTags.COURSES.value, AllureTags.REGRESSION.value)
    def test_add_course_with_o_max_score(self, create_course_page: CreateCoursePage, courses_list_page: CoursesPage):
        create_course_page.visit_create_course_page()
        create_course_page.create_course_form_component.check_visible()
        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.check_exercises_empty_view_visibility()
        create_course_page.upload_image_widget.upload_preview_image(
            settings.test_data.image_png_file)
        create_course_page.create_course_form_component.fill("no estimated time", "12", "course 1 description", None, "2")
        create_course_page.create_course_toolbar_view_component.button.check_disabled()

    @pytest.mark.flaky(reruns=2)
    @allure.severity(Severity.CRITICAL)
    @allure.title("Try to create course with 0 min score")
    @allure.tag(AllureTags.COURSES.value, AllureTags.REGRESSION.value)
    def test_add_course_with_o_min_score(self, create_course_page: CreateCoursePage, courses_list_page: CoursesPage):
        create_course_page.visit_create_course_page()
        create_course_page.create_course_form_component.check_visible()
        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.check_exercises_empty_view_visibility()
        create_course_page.upload_image_widget.upload_preview_image(
            settings.test_data.image_png_file)
        create_course_page.create_course_form_component.fill("no estimated time", "12", "course 1 description", "11", None)
        create_course_page.create_course_toolbar_view_component.button.check_disabled()
