import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Override default browser context args (viewport, base url, etc.)"""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 800},
    }


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the application under test."""
    return "http://example.com"
