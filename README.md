# Playwright Python Automation Framework

This project demonstrates practical UI automation architecture and QA engineering practices using **Playwright, Python, and Pytest**.

It shows a maintainable automation design based on the **Page Object Model (POM)**, reusable UI components, custom element abstractions, Pytest fixtures, cross-browser execution, Allure reporting, and GitHub Actions CI.

The framework is built to demonstrate automation engineering skills while keeping system-level QA principles and exploratory testing strategy as the foundation of product quality.

## Overview

This project automates testing of an LMS-style web application and demonstrates how a UI automation framework can be structured for maintainability and clarity.

Key highlights:

- **Page Object Model (POM)** with layered architecture
- **Reusable UI Components & Custom Elements** to avoid locator duplication
- **Pytest Fixtures** for context and lifecycle management
- **Cross-Browser Testing** support (Chromium, WebKit, Firefox)
- **Parallel Execution** support using `pytest-xdist`
- **Allure Reporting** with step-level metadata
- **GitHub Actions CI** integration
- **Debugging Artifacts:** Screenshots, videos, and Playwright traces for failed test analysis
- **Centralized Configuration & Reusable Test Data**

## Technology Stack

| **Technology**       | **Purpose**                          |
| -------------------- | ------------------------------------ |
| **Python**           | Core test development                |
| **Playwright**       | Browser automation engine            |
| **Pytest**           | Test runner & fixture framework      |
| **pytest-xdist**     | Parallel test execution              |
| **Allure**            | Test reporting                       |
| **GitHub Actions**   | Continuous Integration (CI) pipeline |
| **POM & Components** | Architectural design patterns        |
| **Git**              | Version control                      |

## Framework Architecture

The framework uses a layered approach to separate test intent from UI implementation details:

```text
Tests (Test scenarios & validation)
  ↓
Pages (Page-level workflows)
  ↓
Components (Reusable UI modules)
  ↓
Elements (Custom atomic UI wrappers)
  ↓
Playwright Engine
```

- **Pages:** Expose high-level page operations to test cases.
- **Components:** Encapsulate complex UI blocks such as sidebars, course forms, and toolbars.
- **Elements:** Custom wrappers such as `Button`, `Input`, `FileInput`, and `Textarea` that centralize common UI interaction and validation logic.

## Project Structure

```text
playwright-python-framework/
│
├── .github/
│   └── workflows/
│       └── tests.yaml
│
├── components/
│   ├── authentication/
│   ├── charts/
│   ├── courses/
│   ├── dashboard/
│   ├── navigation/
│   ├── views/
│   ├── base_component.py
│   ├── side_bar_component.py
│   └── side_bar_list_item_component.py
│
├── elements/
│   ├── base_element.py
│   ├── button.py
│   ├── file_input.py
│   ├── icon.py
│   ├── image.py
│   ├── input.py
│   ├── link.py
│   ├── text.py
│   ├── textarea.py
│   └── ui_coverage.py
│
├── fixtures/
├── pages/
├── testdata/
│   ├── files/
│   │   └── image.png
│   └── storage/
│       └── storageState.json
│
├── tests/
│   ├── authentication/
│   ├── courses/
│   ├── dashboard/
│   └── conftest.py
│
├── tools/
│   ├── allure/
│   ├── playwright/
│   ├── environment.py
│   ├── logger.py
│   └── routes.py
│
├── tracing/
├── videos/
├── .env.example
├── config.py
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

## Example Test Scenario

An end-to-end scenario demonstrating high-level test readability supported by Page, Component, and Element abstractions:

```python
@allure.severity(Severity.CRITICAL)
@allure.title("Create course with 2 exercises")
@allure.tag(AllureTags.COURSES.value, AllureTags.REGRESSION.value)
def test_create_course_with_2_exercises(
    self,
    create_course_page: CreateCoursePage,
    courses_list_page: CoursesPage
):
    course_title = "course with 2 exercises"
    course_estimated = "12"
    course_description = "course with two exercises description"
    course_max_score = "11"
    course_min_score = "2"

    exercise_1_title = "exercise 1"
    exercise_1_description = "exercise 1 description"

    exercise_2_title = "exercise 2"
    exercise_2_description = "exercise 2 description"

    create_course_page.visit_create_course_page()
    create_course_page.create_course_form_component.check_visible()
    create_course_page.create_course_exercises_toolbar_view_component.check_visible()
    create_course_page.check_exercises_empty_view_visibility()

    create_course_page.create_course_form_component.fill(
        course_title,
        course_estimated,
        course_description,
        course_max_score,
        course_min_score
    )

    create_course_page.create_course_exercises_toolbar_view_component.create_new_exercise_button.click()

    create_course_page.create_course_exercise_form.fill_create_exercise_form(
        0,
        exercise_1_title,
        exercise_1_description
    )

    create_course_page.create_course_exercises_toolbar_view_component.create_new_exercise_button.click()

    create_course_page.create_course_exercise_form.fill_create_exercise_form(
        1,
        exercise_2_title,
        exercise_2_description
    )

    create_course_page.upload_image_widget.upload_preview_image(
        settings.test_data.image_png_file
    )

    create_course_page.create_course_toolbar_view_component.click_create_course_button()

    courses_list_page.course_view.check_visible(
        index=0,
        title=course_title,
        max_score=course_max_score,
        min_score=course_min_score,
        estimated_time=course_estimated
    )

    courses_list_page.course_view.menu.click_edit(index=0)

    create_course_page.create_course_exercise_form.check_filled_create_exercise_form(
        0,
        exercise_1_title,
        exercise_1_description
    )

    create_course_page.create_course_exercise_form.check_filled_create_exercise_form(
        1,
        exercise_2_title,
        exercise_2_description
    )
```

## Test Execution Commands

| **Command**                                           | **Purpose**                                          |
| ----------------------------------------------------- | ---------------------------------------------------- |
| `pytest`                                              | Execute all tests                                    |
| `pytest -m "regression"`                              | Execute regression suite                             |
| `pytest -m "courses"`                                 | Execute course domain tests                          |
| `pytest -n auto`                                      | Run tests in parallel                                |
| `pytest --headed`                                     | Run tests with visible browser UI                    |
| `pytest tests/courses/test_courses.py`                | Run a specific test file                             |
| `pytest -m "regression" --alluredir=./allure-results` | Run regression tests and generate raw Allure results |

## Allure Reporting & Debugging

Allure decorators provide structured test organization and metadata in reports:

```python
@allure.epic(AllureEpic.LMS.value)
@allure.feature(AllureFeature.COURSES.value)
@allure.story(AllureStories.COURSES.value)
```

To view the generated Allure report locally:

```bash
allure serve allure-results
```

Test artifacts such as screenshots, videos, and Playwright traces are available for debugging test failures.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/grigoriishneer88/playwright-python-framework.git
cd playwright-python-framework
```

### 2. Create and Activate Virtual Environment

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies & Browsers

```bash
pip install -r requirements.txt
playwright install
```

### 4. Run Tests

```bash
pytest -m "regression"
```

## QA Approach & Strategy

- **Risk-Based Coverage:** Focuses on end-to-end validation of critical application flows such as Authentication, Course Creation, Exercise Management, and Course Persistence.
- **Defect Visibility:** Known product issues are explicitly documented using `@pytest.mark.xfail(reason="...")` to keep known defects visible in test reports without treating them as unexpected failures.
- **Balanced QA Mindset:** Test automation is used to cover stable regression workflows, complementing manual exploratory testing and system-level validation.
- **System-Level Thinking:** Test scenarios validate complete user workflows rather than isolated UI interactions, including data persistence and verification after navigation.
- **Maintainability:** Page Objects, reusable Components, and custom Elements separate test intent from UI implementation details.

## Author

**Gregory Shneier**

*Senior QA / V&V Lead | IoT & Multidisciplinary Systems*

- **Focus Areas:** System-Level QA, E2E Validation, Embedded HW/FW/SW Integration, IoT, Medical Devices, QA Infrastructure & Leadership.
- **GitHub:** https://github.com/grigoriishneer88