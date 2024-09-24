from selenium.webdriver.common.by import By

class JobPageLocators:
    SEE_ALL_JOBS=(By.XPATH,"//a[normalize-space()='See all QA jobs']")
    LOCATION_DROPDOWN=(By.XPATH,"//span[@id='select2-filter-by-location-container']")
    LOCATION_OPTION_ISTANBUL=(By.XPATH,"//li[contains(text(), 'Istanbul, Turkey')]")
    DEPARTMENT_DROPDOWN=(By.CSS_SELECTOR,"span[title='Quality Assurance']")
    #DEPARTMENT_DROPDOWN2 = (By.XPATH, "//span[@id='select2-filter-by-department-container']")
    DEPARTMENT_OPTION=(By.XPATH,"//li[contains(text(), 'Quality Assurance')]")
    JOB_LIST=(By.ID,"jobs-list")
    VIEW_ROLE=(By.CSS_SELECTOR,"div#jobs-list>div>div>a")
    POSITION_LIST=(By.CLASS_NAME, "position-list-item")
    FIRST_POSITION=(By.XPATH,"(//div[@class='position-list-item-wrapper bg-light'])[1]")
    QA_POSITION=(By.XPATH,"//*[contains(text(), 'Quality Assurance Engineer')]")

    locator_names={
        "SEE_ALL_JOBS":SEE_ALL_JOBS,
        "LOCATION_DROPDOWN":LOCATION_DROPDOWN,
        "LOCATION_OPTION_ISTANBUL":LOCATION_OPTION_ISTANBUL,
        "DEPARTMENT_DROPDOWN": DEPARTMENT_DROPDOWN,
        "DEPARTMENT_OPTION":DEPARTMENT_OPTION,
        "JOB_LIST":JOB_LIST,
        "VIEW_ROLE":VIEW_ROLE,
        "POSITION_LIST":POSITION_LIST,
        "FIRST_POSITION":FIRST_POSITION,
        "QA_POSITION":QA_POSITION,
    }

