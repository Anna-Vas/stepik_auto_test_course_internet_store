from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    firstname_field = browser.find_element(By.CSS_SELECTOR, "[name = 'firstname']")
    firstname_field.send_keys("Dayana")

    lastname_field = browser.find_element(By.CSS_SELECTOR, "[name = 'lastname']")
    lastname_field.send_keys("Morgan")

    email_field = browser.find_element(By.CSS_SELECTOR, "[name = 'email']")
    email_field.send_keys("silakiski@hotmail.com")

    current_dir = os.path.abspath(os.path.dirname("lesson8_step8.py"))
    file_path = os.path.join(current_dir, 'file.txt')
    file_element = browser.find_element(By.ID, "file")
    file_element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()