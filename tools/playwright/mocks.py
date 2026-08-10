from playwright.sync_api import Page

def mock_status_resources(page: Page):
    page.route("**/*.{ico,png,jpg,svg,webp,mp3,mp4,woff}", lambda route: route.abort())