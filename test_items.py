import time
from selenium.webdriver.common.by import By


class TestProductPage:

    def test_product_page_contains_add2cart_button(self, browser):
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        time.sleep(30)
        add_button_lst = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert len(add_button_lst) > 0, "Add to cart button missing"
