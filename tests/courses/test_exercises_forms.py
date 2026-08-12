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



@pytest.mark.courses
@allure.epic(AllureEpic.LMS.value)
@allure.feature(AllureFeature.COURSES.value)
@allure.story(AllureStories.COURSES.value)
@allure.parent_suite(AllureParentSuite.LMS.value)
@allure.suite(AllureSuite.COURSES.value)
@allure.sub_suite(AllureSubSuite.COURSES.value)
class TestExercisesForms:
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

    @allure.title("Create course with 2 exercises")
    def test_create_course_with_2_exercises(self,
                                            create_course_page: CreateCoursePage,
                                            courses_list_page: CoursesPage
                                            ):
        course_title = 'course with 2 exercises'
        course_estimated = '12'
        course_description = 'course with two exercises description'
        course_max_score = '11'
        course_min_score = '2'

        exercise_1_title = 'exercise 1'
        exercise_1_description = 'exercise 1 description'

        exercise_2_title = 'exercise 2'
        exercise_2_description = 'exercise 2 description'

        create_course_page.visit_create_course_page()
        create_course_page.create_course_form_component.check_visible()
        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.check_exercises_empty_view_visibility()

        # Fill course
        create_course_page.create_course_form_component.fill(
            course_title,
            course_estimated,
            course_description,
            course_max_score,
            course_min_score
        )

        # Create Exercise #1
        create_course_page.create_course_exercises_toolbar_view_component.create_new_exercise_button.click()

        create_course_page.create_course_exercise_form.fill_create_exercise_form(
            0,
            exercise_1_title,
            exercise_1_description
        )

        # Create Exercise #2
        create_course_page.create_course_exercises_toolbar_view_component.create_new_exercise_button.click()

        create_course_page.create_course_exercise_form.fill_create_exercise_form(
            1,
            exercise_2_title,
            exercise_2_description
        )

        # Upload course image
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=False)
        create_course_page.upload_image_widget.upload_preview_image(
            settings.test_data.image_png_file
        )
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=True)

        # Create course
        create_course_page.create_course_toolbar_view_component.click_create_course_button()

        # Verify created course
        courses_list_page.course_view.check_visible(
            index=0,
            title=course_title,
            max_score=course_max_score,
            min_score=course_min_score,
            estimated_time=course_estimated
        )

        # Open Edit
        courses_list_page.course_view.menu.click_edit(index=0)

        # Verify Exercise #1
        create_course_page.create_course_exercise_form.check_filled_create_exercise_form(
            0,
            exercise_1_title,
            exercise_1_description
        )

        # Verify Exercise #2
        create_course_page.create_course_exercise_form.check_filled_create_exercise_form(
            1,
            exercise_2_title,
            exercise_2_description
        )

    @allure.severity(Severity.CRITICAL)
    @allure.title("Delete exercise from course")
    @allure.tag(AllureTags.COURSES.value)
    def test_delete_exercise(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesPage
    ):
        course_title = 'course with deleted exercise'
        course_estimated = '12'
        course_description = 'course with deleted exercise description'
        course_max_score = '11'
        course_min_score = '2'

        exercise_1_title = 'exercise to delete'
        exercise_1_description = 'exercise 1 description'

        exercise_2_title = 'exercise to keep'
        exercise_2_description = 'exercise 2 description'

        create_course_page.visit_create_course_page()

        create_course_page.create_course_form_component.check_visible()
        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.check_exercises_empty_view_visibility()

        # Fill course
        create_course_page.create_course_form_component.fill(
            course_title,
            course_estimated,
            course_description,
            course_max_score,
            course_min_score
        )

        # Create Exercise #1
        create_course_page.create_course_exercises_toolbar_view_component.create_new_exercise_button.click()

        create_course_page.create_course_exercise_form.fill_create_exercise_form(
            0,
            exercise_1_title,
            exercise_1_description
        )

        # Create Exercise #2
        create_course_page.create_course_exercises_toolbar_view_component.create_new_exercise_button.click()

        create_course_page.create_course_exercise_form.fill_create_exercise_form(
            1,
            exercise_2_title,
            exercise_2_description
        )

        # Delete Exercise #1
        create_course_page.create_course_exercise_form.click_delete_button(0)

        # Verify Exercise #2 remains after deleting Exercise #1
        create_course_page.create_course_exercise_form.check_filled_create_exercise_form(
            0,
            exercise_2_title,
            exercise_2_description
        )

        # Save course
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=False)
        create_course_page.upload_image_widget.upload_preview_image(
            settings.test_data.image_png_file
        )
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=True)

        create_course_page.create_course_toolbar_view_component.click_create_course_button()

        # Open Edit
        courses_list_page.course_view.menu.click_edit(index=0)

        # Verify Exercise #2 persisted
        create_course_page.create_course_exercise_form.check_filled_create_exercise_form(
            0,
            exercise_2_title,
            exercise_2_description
        )

    @allure.severity(Severity.CRITICAL)
    @allure.title("Edit exercise")
    @allure.tag(AllureTags.COURSES.value)
    def test_edit_exercise(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesPage
    ):
        course_title = 'course with edited exercise'
        course_estimated = '12'
        course_description = 'course description'
        course_max_score = '11'
        course_min_score = '2'

        exercise_title = 'exercise 1'
        exercise_description = 'exercise 1 description'

        edited_exercise_title = 'edited exercise 1'
        edited_exercise_description = 'edited exercise 1 description'

        create_course_page.visit_create_course_page()

        create_course_page.create_course_form_component.check_visible()
        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.check_exercises_empty_view_visibility()

        # Fill course
        create_course_page.create_course_form_component.fill(
            course_title,
            course_estimated,
            course_description,
            course_max_score,
            course_min_score
        )

        # Create Exercise
        create_course_page.create_course_exercises_toolbar_view_component.create_new_exercise_button.click()

        create_course_page.create_course_exercise_form.fill_create_exercise_form(
            0,
            exercise_title,
            exercise_description
        )

        # Upload course image
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=False)
        create_course_page.upload_image_widget.upload_preview_image(
            settings.test_data.image_png_file
        )
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=True)

        # Create course
        create_course_page.create_course_toolbar_view_component.click_create_course_button()

        # Open Edit
        courses_list_page.course_view.menu.click_edit(index=0)

        # Edit Exercise
        create_course_page.create_course_exercise_form.fill_create_exercise_form(
            0,
            edited_exercise_title,
            edited_exercise_description
        )

        # Save course
        create_course_page.create_course_toolbar_view_component.click_create_course_button()

        # Open Edit again
        courses_list_page.course_view.menu.click_edit(index=0)

        # Verify edited Exercise persisted
        create_course_page.create_course_exercise_form.check_filled_create_exercise_form(
            0,
            edited_exercise_title,
            edited_exercise_description
        )