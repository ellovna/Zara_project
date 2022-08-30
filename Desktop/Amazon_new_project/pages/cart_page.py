from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CartPage(Page):

    CART_ITEM = (By. CSS_SELECTOR, "div[class='a-section a-padding-medium sw-atc-message-section']")

    def cart_verify(self):
        assert self.driver.find_element(*self. CART_ITEM), 'Error, not found'




