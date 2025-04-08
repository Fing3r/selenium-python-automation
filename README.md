# Selenium Python Automation

This project is a Selenium-based Python automation framework designed for testing web applications. It includes test cases for login functionality and uses Pytest for test execution.

## Project Structure

selenium-python-automation/
├── pages/              # Page Object classes
│   ├── init.py     # Makes 'pages' a Python package
│   └── login_page.py   # Page Object Model for the login page
├── tests/              # Test scripts and logs
│   ├── test_login.py   # Test cases for login functionality
│   └── test_log.log    # Log file for test results
├── .vscode/            # VS Code configuration
│   ├── launch.json     # VS Code debug configuration
│   └── settings.json   # VS Code settings
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation


### Key Directories and Files

- **`pages/`**: Contains page object models for the application under test.
  - `login_page.py`: Implements the `LoginPage` class for interacting with the login page.

- **`tests/`**: Contains test cases.
  - `test_login.py`: Includes test cases for valid and invalid login scenarios.

- **`.vscode/`**: Contains VS Code configuration files for debugging and settings.

- **`requirements.txt`**: Lists the Python dependencies required for the project.

## Prerequisites

- Python 3.10 or higher
- Google Chrome and ChromeDriver
- Virtual environment (optional but recommended)

## Installation

1. Clone the repository:
   git clone https://github.com/Fing3r/selenium-python-automation.git
   cd selenium-python-automation

2. Create and activate virtual enviroment: 
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install dependencies:
    pip install -r requirements.txt

## Running Tests:
pytest tests/ -v

## Run a specific test:
pytest tests/test_login.py::test_valid_login -v

Debugging
Use the provided .vscode/launch.json configuration to debug tests in Visual Studio Code.

Features
Page Object Model: Encapsulates web elements and actions in pages/login_page.py.
Pytest Integration: Simplifies test execution and reporting.
Logging: Logs test results in test_log.log.
License
This project is licensed under the MIT License.
