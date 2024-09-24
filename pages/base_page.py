from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import setup_logger


class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.timeout=30
        self.logger=setup_logger(self.__class__.__name__)

    def click(self, locator, timeout=10):
        try:
            # Locator'ın adını bulmak için dictionary'de arama yapıyoruz
            locator_name = None
            if hasattr(self, 'locators') and hasattr(self.locators, 'locator_names'):
                locator_name = next((name for name, loc in self.locators.locator_names.items() if loc == locator), None)

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()

            # Locator adını log'a ekliyoruz
            self.logger.debug(f'Clicking element: {locator_name or locator}')
        except Exception as e:
            self.logger.error(f'Error clicking element: {locator}. Exception: {e}')

    def wait_for_element(self, locator,timeout=10):
        self.logger.debug(f'Waiting for element: {locator}')
        WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_title(self,expected_title,timeout=20):
        self.logger.debug(f'Waiting for title: {expected_title}')
        WebDriverWait(self.driver,timeout).until(EC.title_is(expected_title))

    def is_element_visible(self, locator):
        try:
            self.wait_for_element(locator)
            self.logger.debug(f'Element is visible:{locator}')
            return self.driver.find_element(*locator).is_displayed()
        except Exception as e:
            self.logger.error(f'Element is not visible:{locator}- Error: {e}')
            return False

    def get_page_title(self):
        self.logger.debug('Getting page title')
        return self.driver.title

    def verify_page_title(self,expected_title):
        actual_title=self.get_page_title()
        self.logger.debug(f'Verifying page title: Expected: "{expected_title}" - Actual: "{actual_title}"')
        assert actual_title == expected_title, f"Expected title '{expected_title}' but got '{actual_title}'"
