from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    x_field = browser.find_element(By.ID, "answer")
    x_field.send_keys(y)

    check_field = browser.find_element(By.ID, "robotCheckbox")
    check_field.click()

    radio_field = browser.find_element(By.ID, "robotsRule")
    radio_field.click()

    button_field = browser.find_element(By.TAG_NAME, "button")
    button_field.click()

finally:
    time.sleep(10)
    browser.quit()