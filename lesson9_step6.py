from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    button = browser.find_element(By.CLASS_NAME, "trollface")
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer_value = calc(x)

    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(answer_value)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    print(browser.switch_to.alert.text)

finally:
    time.sleep(3)
    browser.quit()