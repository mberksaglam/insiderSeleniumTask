from selenium.common import TimeoutException
from locators.home_page_locators import HomePageLocators
from .base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators()

    def is_open(self):
        return self.is_element_visible(self.locators.LOGO)

    def cookie_accept(self):
        self.click(self.locators.COOKIE_ACCEPT)
        return True
    def navigate_to_careers(self):
        self.logger.debug('Navigating to Company -> Careers page')

        try:
            self.click(self.locators.NavBar_COMPANY)

            self.click(self.locators.NavBar_COMPANY_CAREERS)

            return True
        except TimeoutException:
            self.logger.error("Failed to clicked to Careers menu")
            return False
        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            return False

