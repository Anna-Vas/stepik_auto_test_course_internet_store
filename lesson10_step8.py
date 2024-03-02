from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)

try:
    price_element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer_value = calc(x)

    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(answer_value)

    solve_button = browser.find_element(By.ID, "solve")
    solve_button.click()

    print(browser.switch_to.alert.text)

finally:
    time.sleep(3)
    browser.quit()