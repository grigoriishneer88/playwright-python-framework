from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.side_bar_component import SideBarComponent
from pages.base_page import BasePage
from playwright.sync_api import Page

from tools.routes import AppRoute


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.dashboard_toolbar_view_component = DashboardToolbarViewComponent(page)
        self.students_chart_view = ChartViewComponent(page, "students", "bar")
        self.activities_chart_view = ChartViewComponent(page, "activities", "line")
        self.courses_chart_view = ChartViewComponent(page, "courses", "pie")
        self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")
        self.navbar_component = NavbarComponent(page)
        self.side_bar_component = SideBarComponent(page)

    def visit_dashboard_page(self):
        self.visit(AppRoute.DASHBOARD)
