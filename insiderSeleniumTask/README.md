# 📜 Insider Selenium Case with Python 📜

This project is designed for automated testing of the **Insider web application**. It uses a **Page Object Model (POM)** structure to organize test cases and page elements effectively. The tests are developed using **Selenium** and **Python** with the **unittest** framework, ensuring clear separation of concerns and maintainability.

## Directory Structure
```plaintext
InsiderSeleniumTask/
│
├── locators/
│   ├── __init__.py                 # Package initialization
│   ├── careers_page_locators.py    # Locators for the careers page
│   ├── home_page_locators.py       # Locators for the home page
│   └── job_page_locators.py        # Locators for the job page
│
├── pages/
│   ├── __init__.py                 # Package initialization
│   ├── base_page.py                # Base page class for shared functionality
│   ├── careers_page.py             # Page object for the careers page
│   ├── home_page.py                # Page object for the home page
│   └── job_page.py                 # Page object for the job page
│
├── tests/
│   ├── __init__.py                 # Package initialization
│   └── test_home.py                # Test cases for the home page
│
├── utils/
│   ├── __init__.py                 # Package initialization
│   ├── browser_setup.py            # Browser setup and configuration
│   └── logger.py                   # Logging utility
│
├── requirements.txt            # Python package dependencies
└── test_log.log                # Log file for test results

```



### Installation
```bash
To install the required dependencies, run:

pip install -r requirements.txt
```

### Usage
#### If you want to run all tests, you should type: 

```bash
python -m unittest 
```

#### If you want to run just a test method, you should type:

```bash
python -m unittest tests/test_home.py
```
## 📜 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.






