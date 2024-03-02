from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


link = "https://en.wikipedia.org/wiki/Main_Page"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)

try:
    # search_query = input("Input your query: ")

    initiate_search_button = browser.find_element(By.CSS_SELECTOR, "[accesskey='f']")
    initiate_search_button.click()

    search_field = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='search' and @name='search' and @accesskey='f']"))
    )
    search_field.send_keys("cat")

    search_button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cdx-search-input__end-button"))
    )
    search_button.click()

    time.sleep(10)

finally:
    time.sleep(3)
    browser.quit()