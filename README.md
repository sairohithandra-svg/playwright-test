# Playwright + Pytest Test Suite

End-to-end browser tests using [Playwright](https://playwright.dev/python/) with [pytest](https://docs.pytest.org/).

## Project Structure

```
.
├── conftest.py          # Shared fixtures (base_url, browser context settings)
├── pytest.ini           # Pytest configuration (markers, default options)
├── requirements.txt     # Python dependencies
└── tests/
    └── test_homepage.py # Sample tests
```

## Setup

```bash
# 1. Create a virtual environment
python3 -m venv venv
source venv/bin/activate      # Mac/Linux
# venv\Scripts\activate        # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install Playwright browsers
playwright install
```

## Running Tests

```bash
# Run all tests
pytest

# Run with visible browser (headed mode)
pytest --headed

# Run a specific test file
pytest tests/test_homepage.py

# Run tests matching a marker
pytest -m smoke

# Run with a different browser
pytest --browser firefox
pytest --browser webkit

# Generate HTML report
pytest --html=report.html --self-contained-html
```

## Writing New Tests

Add new test files under `tests/`, following the `test_*.py` naming convention.
Use the `page` fixture (provided by `pytest-playwright`) to interact with the browser,
and the `base_url` fixture (defined in `conftest.py`) for the app under test.

```python
def test_example(page, base_url):
    page.goto(base_url)
    # your assertions here
```

## CI/CD

This project is designed to run inside a Jenkins pipeline. Typical pipeline steps:

```groovy
stage('Install') {
    steps {
        sh 'pip install -r requirements.txt'
        sh 'playwright install --with-deps'
    }
}

stage('Test') {
    steps {
        sh 'pytest --html=report.html --self-contained-html'
    }
}
```
