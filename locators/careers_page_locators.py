from selenium.webdriver.common.by import By

class CareersPageLocators:
    CAREERS_PAGE_TITLE = "Ready to disrupt? | Insider Careers"
    TEAMS_BLOCK = (By.CSS_SELECTOR, '[data-id="b6c45b2"]')
    LOCATIONS_BLOCK = (By.CSS_SELECTOR, '[data-id="8ab30be"]')
    LIFE_BLOCK = (By.CSS_SELECTOR, '[data-id="a8e7b90"]')

    locator_names = {
    "CAREERS_PAGE_TITLE":CAREERS_PAGE_TITLE,
    "TEAMS_BLOCK":TEAMS_BLOCK,
    "LOCATIONS_BLOCK":LOCATIONS_BLOCK,
    "LIFE_BLOCK":LIFE_BLOCK
    }

