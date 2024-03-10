from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import math

links = ["https://stepik.org/lesson/236895/step/1",  # 1
         "https://stepik.org/lesson/236896/step/1",  # 2
         "https://stepik.org/lesson/236897/step/1",  # 3
         "https://stepik.org/lesson/236898/step/1",  # 4
         "https://stepik.org/lesson/236899/step/1",  # 5
         "https://stepik.org/lesson/236903/step/1",  # 6
         "https://stepik.org/lesson/236904/step/1",  # 7
         "https://stepik.org/lesson/236905/step/1"]  # 8

@pytest.mark.parametrize('link', links)
def test_login_on_stepik(browser, link):
    browser.get(link)
    button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "navbar__auth_login"))
    )
    button.click()
    email_field = browser.find_element(By.ID, "id_login_email")
    email_field.send_keys("<email>")  # substitute <email> for your email
    password_field = browser.find_element(By.ID, "id_login_password")
    password_field.send_keys("<password>")  # substitute <password> for your Stepik password
    button_submit = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    button_submit.click()
    #answer_field = WebDriverWait(browser, 5).until(
    #    EC.presence_of_element_located((By.CLASS_NAME, "string-quiz__textarea"))
    #)
    time.sleep(10)
    answer_field = browser.find_element(By.CLASS_NAME, "string-quiz__textarea")
    answer = str(math.log(int(time.time())))
    answer_field.send_keys(answer)
    #button_submit_answer = WebDriverWait(browser, 5).until(
    #    EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    #)
    time.sleep(3)
    button_submit_answer = browser.find_element(By.CLASS_NAME, "submit-submission")
    button_submit_answer.click()
    #feedback = WebDriverWait(browser, 5).until(
    #    EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    #)
    time.sleep(5)
    feedback = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    feedback_text = feedback.text
    correct_text = "Correct!"
    assert feedback_text == correct_text, f"Answer should be '{correct_text}' but is '{feedback_text}'"
