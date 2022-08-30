from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class SearchPage(Page):

    SEARCH = (By. ID, "twotabsearchtextbox")
    SNEAKERS = (By. CSS_SELECTOR, "div[data-component-type='s-search-result']")
    SIZE = (By. CSS_SELECTOR, "span[class='twister-dropdown-highlight transparentTwisterDropdownBorder']")
    # CORRECT_SIZE = (By. CSS_SELECTOR, "div[class='a-popover a-dropdown a-dropdown-common a-declarative']")
    #CORRECT_SIZE = (By. XPATH, "//a[text = '8']")
    #SIZE_OPTION = (By. ID, "#size_name_13")
    ADD_TO_CART = (By. ID, "add-to-cart-button")
    CORRECT_SIZE = (By. XPATH, '//a[text()="10.5"]')

    def search_for_nike_shoes(self):
        e = self.driver.find_element(*self. SEARCH)
        e.clear()
        e.send_keys("Nike Men's Shoes")
        e.send_keys(Keys.ENTER)

    def click_sneakers(self):
        all_shoes = self.driver.find_elements(*self. SNEAKERS)
        sleep(3)
        all_shoes[4].click()

        # for cell in all_shoes:
        #     if "Nike" in cell.text:
        #         print("Nike found")
        #         cell.click()
        #
        #     else:
        #         print('No Nike shoes found')

    def click_size(self):
        self.driver.find_element(*self.SIZE).click()
        self.wait_for_element_appear(*self.SIZE)

    def click_correct_size(self):
        self.driver.find_element(*self. CORRECT_SIZE).click()
        sleep(10)
        # expected_size = [8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5]
        # actual_size = []
        #
        # size_options = self.driver.find_elements(*self.CORRECT_SIZE)
        # for options in size_options:
        #     options.click()
        #     size = self.driver.find_element(*self.SIZE_OPTION)
        #     actual_size += [size_options]
        # element = self.wait.until(EC.element_to_be_clickable(*self.CORRECT_SIZE))
        # for item in element:
        #     if 10.5 in item:
        #         item.click()

    def add_to_cart_item(self):
        self.driver.find_element(*self. ADD_TO_CART).click()



