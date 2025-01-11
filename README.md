# Python Selenium Test Project

This project contains automated tests using Python, Selenium, and Pytest.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Chrome/Firefox browser (depending on your webdriver configuration)

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate

#Install Dependencies
pip install -r requirements.txt

## Project Structure
PYTHON SELENIUM/
├── config/         # Configuration files
├── drivers/        # WebDriver files
├── pages/          # Page Object files
├── tests/          # Test files
│   ├── test_login.py
│   └── conftest.py
└── requirements.txt

## Run all tests:
pytest

## To run specific test file:
pytest tests/test_login.py -v

## To run tests and see print statements:
pytest tests/test_login.py -v -s
