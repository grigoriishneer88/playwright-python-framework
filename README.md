# Playwright Python Automation Framework

This project demonstrates a scalable UI automation framework built with Playwright, Python and Pytest. The project demonstrates a scalable automation architecture using Page Object Model, reusable fixtures, parallel execution, GitHub Actions CI and Allure reporting.

The test application source code is available on [GitHub](https://github.com/Nikita-Filonov/qa-automation-engineer-ui-course).

## Overview


The framework automates testing of the UI Course application while demonstrating maintainable automation practices.

It is built using the Page Object Model pattern and includes reusable fixtures, test parametrization, parallel execution, configuration management and CI integration.

## Technology Stack

- Playwright
- Python
- Pytest
- Page Object Model (POM)
- Pytest Fixtures
- pytest-xdist
- Allure Reports
- GitHub Actions


## Getting Started

### Clone the Repository

To get started, clone the project repository using Git:

```bash
git clone https://github.com/grigoriishneer88/playwright-python-framework.git
cd playwright-python-framework
```

### Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies. Follow the instructions for your operating
system:

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

Once the virtual environment is activated, install the project dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```


### Install Playwright Browsers
```bash
playwright install
```

### Running Tests

To execute regression tests and generate Allure results, run:

```bash
pytest -m "regression" --alluredir=./allure-results
```

This will execute all tests in the project and display the results in the terminal.

### Additional Examples

```bash
pytest

pytest -m smoke

pytest -m regression

pytest -n auto

pytest --headed
```

### Viewing the Allure Report

After the test execution, generate and open the Allure report by running:

```bash
allure serve allure-results
```

This command will open the Allure report in your default web browser.
