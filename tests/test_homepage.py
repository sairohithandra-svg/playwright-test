import re
from playwright.sync_api import Page, expect


def test_homepage_title(page: Page, base_url):
    """Verify the homepage loads and has the expected title."""
    page.goto(base_url)
    expect(page).to_have_title(re.compile("Example Domain"))


def test_homepage_heading(page: Page, base_url):
    """Verify the main heading is visible on the page."""
    page.goto(base_url)
    heading = page.get_by_role("heading", name="Example Domain")
    expect(heading).to_be_visible()


def test_more_info_link(page: Page, base_url):
    """Verify at least one link exists on the page."""
    page.goto(base_url)
    links = page.get_by_role("link")
    expect(links.first).to_be_visible()
