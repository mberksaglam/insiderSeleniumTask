import time
from selenium.webdriver.support import expected_conditions as EC
from locators.job_page_locators import JobPageLocators
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class JobPage(BasePage):
    def __init__(self, driver):
        # Constructor to initialize driver and locators
        super().__init__(driver)
        self.locators = JobPageLocators()
        self.url = "https://useinsider.com/careers/quality-assurance/"

    def click_see_all_jobs(self):
        """ Clicks the 'See All Jobs' button and navigates to the job listing page. """
        try:
            # Open the career page
            self.driver.get(self.url)
            # Wait until 'See All Jobs' button is clickable, then click it
            self.click(self.locators.SEE_ALL_JOBS)
            return True
        except TimeoutException:
            self.logger.error("Timeout while clicking 'See all QA jobs'")
            return False

    def select_location(self):
        """ Selects 'Istanbul, Turkey' from the location dropdown and 'Quality Assurance' from the department dropdown. """
        try:
            #I dont want use this but there is problem loading the page
            time.sleep(5)  # Pause to allow page to load

            """WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators.DEPARTMENT_DROPDOWN)
            )"""
            self.wait_for_element(self.locators.DEPARTMENT_DROPDOWN)
            #self.wait_for_element(self.locators.QA_POSITION)
            self.logger.debug("Page is loaded.'Quality Assurance Department Dropdown AND Job List checked'")
            # Select location dropdown and click to expand
            self.click(self.locators.LOCATION_DROPDOWN)

            # Select Istanbul, Turkey from the dropdown options
            self.click(self.locators.LOCATION_OPTION_ISTANBUL)

            self.wait_for_element(self.locators.JOB_LIST)
            self.wait_for_element(self.locators.FIRST_POSITION)

            # Select department dropdown and click to expand
            #self.click(self.locators.DEPARTMENT_DROPDOWN)
            # Select Quality Assurance from the department dropdown|||| Case'de Yazılmamış ama yazmak gerekeblir
            """qa_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.DEPARTMENT_OPTION)
            )
            if qa_option.text == "Quality Assurance":
                qa_option.click()
                return True
            else:
                self.logger.error("Cannot select 'Quality Assurance'")
                return False"""
            return True

        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            return False

    def check_all_jobs(self):
        """ Verifies that 'Quality Assurance' jobs in 'Istanbul, Turkey' are listed and moves the mouse over the job element. """
        time.sleep(5)
        try:
            # Wait until job listings are visible
            self.wait_for_element(self.locators.POSITION_LIST)

            positions = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "position-list-item"))
            )

            # Iterate through all positions to find the matching job
            for position in positions:
                title_text = position.find_element(By.CLASS_NAME, "position-title").text
                department_text = position.find_element(By.CLASS_NAME, "position-department").text
                location_text = position.find_element(By.CLASS_NAME, "position-location").text

                # Check if the job matches 'Quality Assurance' in 'Istanbul, Turkey'
                if "Quality Assurance" in title_text and "Quality Assurance" in department_text and "Istanbul, Turkey" in location_text:
                    self.logger.debug(
                        f"Matched position: {title_text}, Department: {department_text}, Location: {location_text}")

                    # Move mouse to the matched job element then I want click view role
                    actions = ActionChains(self.driver)
                    actions.move_to_element(position).perform()
                    return True
                else:
                    self.logger.error(
                        f"Non-matching position: {title_text}, Department: {department_text}, Location: {location_text}")

            return False

        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            return False
    def scroll_down_page(self, scroll_pause_time=1, max_scrolls=10):
        """ Scrolls down the page to load more job listings, if applicable. """
        try:
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            scrolls = 0

            # Scroll the page multiple times, up to max_scrolls
            while scrolls < max_scrolls:
                self.driver.execute_script("window.scrollTo(0, 400);")
                time.sleep(scroll_pause_time)  # Wait for page content to load

                # Check if the page height has changed after scrolling
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break  # Stop scrolling if no new content is loaded
                last_height = new_height
                scrolls += 1

            self.logger.debug("Successfully scrolled down the page")
            return True
        except Exception as e:
            self.logger.error(f"Error while scrolling down the page: {e}")
            return False


    def click_view_role(self):
        """ Clicks the 'View Role' button, switches to the newly opened tab, and verifies the URL. """
        try:
            # Wait until 'View Role' button is clickable and then click it
            """view_role_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.VIEW_ROLE)
            )
            view_role_button.click()"""
            self.click(self.locators.VIEW_ROLE)

            # Wait for the new tab to open
            WebDriverWait(self.driver, 10).until(
                lambda d: len(d.window_handles) > 1  # Check if new tab is opened
            )

            # Switch to the newly opened tab
            new_tab = self.driver.window_handles[-1]
            self.driver.switch_to.window(new_tab)

            # Wait for the new page to load and verify the URL
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("jobs.lever.co")
            )

            current_url = self.driver.current_url
            if current_url.startswith("https://jobs.lever.co/"):
                self.logger.debug(f"Successfully navigated to {current_url} in the new tab")
                return True
            else:
                self.logger.error(f"Unexpected URL in the new tab after clicking 'View Role': {current_url}")
                return False

        except TimeoutException:
            self.logger.error("Timeout while clicking 'View Role' or waiting for the new tab to load")
            return False
        except Exception as e:
            self.logger.error(f"An unexpected error occurred while switching to the new tab or verifying URL: {e}")
            return False
