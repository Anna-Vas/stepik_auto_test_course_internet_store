from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/find_xpath_form"
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Vernite Cosmetos")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
