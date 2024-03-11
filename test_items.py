from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_exists_add_to_cart_button(browser):
    browser.get(link)
    add_to_cart_button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert add_to_cart_button != [], "'Add to cart' button not found."