from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from locators.careers_page_locators import CareersPageLocators

class CareersPage(BasePage):
    def __init__(self, driver):
        """
        Initialize the CareersPage object with a WebDriver instance.

        :param driver: WebDriver instance to control the browser.
        """
        super().__init__(driver)
        self.locators = CareersPageLocators()

    def check_page_loaded(self):
        """
        Check if the Careers page has loaded successfully by verifying the title.

        :return: True if the page is loaded successfully, False otherwise.
        """
        try:
            # Wait until the Careers page title is present in the browser title.
            """WebDriverWait(self.driver, 10).until(
                lambda driver: CareersPageLocators.CAREERS_PAGE_TITLE in driver.title
            )"""
            #self.wait_for_title(CareersPageLocators.CAREERS_PAGE_TITLE)
            current_url = self.driver.current_url
            if current_url.startswith("https://useinsider.com/careers/"):
                self.logger.debug(f"Successfully navigated to {current_url} in the new tab")
                return True
            else:
                self.logger.error(f"Unexpected URL in the new tab after clicking 'View Role': {current_url}")
                return False
        except TimeoutException:
            self.logger.error("Page title of careers page does not match")  # Log timeout error
            return False
        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")  # Log unexpected errors
            return False

    def are_blocks_visible(self):
        """
        Check if the required blocks on the Careers page are visible.

        :return: True if all specified blocks are visible, False otherwise.
        """
        blocks = {
            'Teams Block': self.locators.TEAMS_BLOCK,
            'Locations Block': self.locators.LOCATIONS_BLOCK,
            'Life Block': self.locators.LIFE_BLOCK
        }

        visibility_results = []

        # Check visibility of all blocks and log if any block is not visible.
        for name, locator in blocks.items():
            try:
                self.wait_for_element(locator)  # wait_for_element ile görünürlüğü bekliyoruz
                visibility_results.append(True)
                self.logger.debug(f"{name} is visible.")  # Blok görünüyorsa logla
            except Exception as e:
                visibility_results.append(False)
                self.logger.error(f"{name} is not visible. Error: {e}")  # Hata mesajını logla

        # Return True if all blocks are visible, otherwise return False.
        return all(visibility_results)

    """def are_blocks_visible(self):
        
        #Check if the required blocks on the Careers page are visible.

        #:return: True if all specified blocks are visible, False otherwise.
        
        blocks = {
            'Teams Block': self.locators.TEAMS_BLOCK,
            'Locations Block': self.locators.LOCATIONS_BLOCK,
            'Life Block': self.locators.LIFE_BLOCK
        }

        # Check visibility of all blocks and log if any block is not visible.
        visibility_results = [
            self.is_element_visible(locator) or self.logger.error(f"{name} is not visible.")
            for name, locator in blocks.items()
        ]

        # Return True if all blocks are visible, otherwise return False.
        return all(visibility_results)"""
