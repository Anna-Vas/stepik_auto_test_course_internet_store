from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer_value = calc(x)

    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(answer_value)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox_field = browser.find_element(By.ID, "robotCheckbox")
    checkbox_field.click()

    radio_field = browser.find_element(By.ID, "robotsRule")
    radio_field.click()

    button.click()
finally:
    time.sleep(10)
    browser.quit()