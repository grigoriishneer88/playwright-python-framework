import allure
from playwright.sync_api import Playwright

from config import settings, Browser
from tools.playwright.mocks import mock_status_resources


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        storage_stage: str | None,
        browser_type: Browser
):
    browser = None
    context = None
    page = None
    try:
        browser = playwright[browser_type].launch(headless=settings.headless)
        context = browser.new_context(base_url=settings.get_base_url(), storage_state=storage_stage,
                                      record_video_dir=settings.videos_dir)
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        mock_status_resources(page)

        yield page
    finally:
        trace_file = settings.tracing_dir.joinpath(f'{test_name}.zip')
        context.tracing.stop(path=trace_file)
        allure.attach.file(str(trace_file), name="trace", attachment_type=allure.attachment_type.ZIP)
        video_path = page.video.path()
        context.close()
        browser.close()
        if video_path:
            allure.attach.file(video_path, name='video', attachment_type=allure.attachment_type.WEBM)
