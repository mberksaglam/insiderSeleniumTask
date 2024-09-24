from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def create_driver():
    options = webdriver.ChromeOptions()
    ##user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.59 Safari/537.36"
    ##options.add_argument(f"user-agent={user_agent}")
    ##options.add_argument("--headless")  # Tarayıcıyı görünmez çalıştırmak için
    options.add_argument("--no-sandbox")
    ##options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    ##options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    return driver

