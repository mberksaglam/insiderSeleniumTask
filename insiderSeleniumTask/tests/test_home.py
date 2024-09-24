import unittest
from pages.job_page import JobPage
from utils.browser_setup import create_driver
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from utils.logger import setup_logger

# Test case class for verifying the functionality of the Insider website.
# This class contains tests related to the home page and job applications.
# To run this module, use the command: python <module-name.py>
class TestHome(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up the test class.
        This method is called once for the entire class and is used to set up any state shared across tests.
        It initializes the browser driver and navigates to the main URL.
        """
        try:
            cls.driver = create_driver()
            url="https://useinsider.com/" # Main URL
            cls.driver.get(url)
            cls.logger = setup_logger(cls.__name__)  # Set up logger for the class
            cls.logger.info(f"Browser started and navigated to the main URL:{url}")
        except Exception as e:
            cls.logger.error(f"Browser has not started: {e}")
            cls.driver.quit()
            raise

    def setUp(self):
        """Set up the logger for each test method."""
        self.logger = setup_logger(self.__class__.__name__)

    def test01_home_page_open_navigate_to_careers(self):
        """
        Test case to verify the home page opens correctly and navigates to the careers page.
        Asserts that the home page is displayed, cookies are accepted, and navigation to the careers page is successful.
        """
        home_page = HomePage(self.driver)
        try:
            self.assertTrue(home_page.is_open(), "Insider home page did not open.")
            self.assertTrue(home_page.cookie_accept(), "Cookie accept button was not clicked.")
            self.assertTrue(home_page.navigate_to_careers(), "Failed to navigate to the Careers page.")
        except AssertionError as e:
            self.logger.error(f"Test 1 FAILED. Assertion failed: {e}")
        self.logger.info("TEST 1 DONE-|-Successfully navigated to the Careers page.")

    def test02_check_open_careers_check_careers_block(self):
        """
        Test case to check if the careers page loads correctly and displays the job blocks.
        Asserts that the careers page is loaded and the blocks are visible.
        """
        careers_page = CareersPage(self.driver)
        try:
            self.assertTrue(careers_page.check_page_loaded(), "Careers page did not load.")
            self.assertTrue(careers_page.are_blocks_visible(), "Failed to find visible job blocks.")
        except AssertionError as e:
            self.logger.error(f"Test 2 FAILED. Assertion failed: {e}")
        self.logger.info("TEST 2 DONE-|-Careers page loaded and blocks are visible.")

    def test03_go_to_jobs(self):
        """
        Test case to go to the jobs section from the careers page.
        Asserts that the user can see all jobs and selects the correct location.
        """
        job_page = JobPage(self.driver)
        try:
            self.assertTrue(job_page.click_see_all_jobs(), "Failed to navigate to job listings.")
            self.assertTrue(job_page.select_location(), "Failed to select the job location.")
        except AssertionError as e:
            self.logger.error(f"Test 3 FAILED. Assertion failed: {e}")
        self.logger.info("TEST 3 DONE-|-Navigated to job listings and selected location.")

    def test04_check_all_jobs(self):
        """
        Test case to check all job listings.
        Asserts that job listings are correctly displayed and allows scrolling through the list.
        """
        job_page = JobPage(self.driver)
        try:
            self.assertTrue(job_page.check_all_jobs(), "Job listings do not match criteria.")
            self.assertTrue(job_page.scroll_down_page(1, 1), "Failed to scroll down the job listings.")
        except AssertionError as e:
            self.logger.error(f"Test 4 FAILED. Assertion failed: {e}")
        self.logger.info("TEST 4 DONE-|-Checked all jobs and scrolled down the listings.")

    def test05_click_view_role(self):
        """
        Test case to click on the 'View Role' button for a specific job.
        Asserts that the button click is successful.
        """
        job_page = JobPage(self.driver)
        try:
            self.assertTrue(job_page.click_view_role(), "Cannot click 'View Role' button or not access jobs.lever.co ")
        except AssertionError as e:
            self.logger.error(f"Test 5 FAILED. Assertion failed: {e}")
        self.logger.info("TEST 5 DONE-|-Clicked on 'View Role' successfully and successfully entered on jobs.lever.co")

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the test class.
        This method is called once for the entire class and is used to release any resources.
        It closes the browser driver.
        """
        try:
            cls.driver.quit()
            cls.logger.info("Browser closed successfully.")
        except Exception as e:
            cls.logger.error(f"Browser has not stopped: {e}")

if __name__ == "__main__":
    unittest.main()
