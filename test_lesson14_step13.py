from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        name_field = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required='']")
        name_field.send_keys("Ivan")

        lastname_field = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required='']")
        lastname_field.send_keys("Pupkin")

        email_field = browser.find_element(By.XPATH, "//input[@class='form-control third' and @required='']")
        email_field.send_keys("pupkinvanya@mail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration wasn't complete.")

        browser.quit()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        name_field = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required='']")
        name_field.send_keys("Ivan")

        lastname_field = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required='']")
        lastname_field.send_keys("Pupkin")

        email_field = browser.find_element(By.XPATH, "//input[@class='form-control third' and @required='']")
        email_field.send_keys("pupkinvanya@mail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration wasn't complete.")

        browser.quit()

if __name__ == "__main__":
    unittest.main()
