from playwright.sync_api import Page

from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage


class CoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.course_view = CourseViewComponent(page)
        self.empty_view = EmptyViewComponent(page,'courses-list')
        self.toolbar_view_component = CoursesListToolbarViewComponent(page)
        self.navbar_component = NavbarComponent(page)
        self.create_course_toolbar_view_component = CreateCourseToolbarViewComponent(page)



    def check_empty_view_visibility(self):
        self.empty_view.check_visible(title = "There is no results",
                                      description="Results from the load test pipeline will be displayed here"
                                      )
