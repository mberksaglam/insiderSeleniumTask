from selenium.webdriver.common.by import By

class HomePageLocators:
    LOGO = (By.XPATH, "//img[@alt='insider_logo']")
    NavBar_COMPANY = (By.XPATH, "//div[@id='navbarNavDropdown']/ul[1]/li[6]/a[1]")
    NavBar_COMPANY_CAREERS = (By.XPATH, "//a[@href='https://useinsider.com/careers/']")
    COOKIE_ACCEPT = (By.XPATH,"//a[@id='wt-cli-accept-all-btn']")

    locator_names={
        "LOGO":LOGO,
        "NavBar_COMPANY":NavBar_COMPANY,
        "NavBar_COMPANY_CAREERS":NavBar_COMPANY_CAREERS,
        "COOKIE_ACCEPT":COOKIE_ACCEPT
    }