from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.partition("&")[0]

    def add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        basket_btn.click()

    def should_be_message_with_name_for_added_product(self, name):
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        expected_message = name + " has been added to your basket"
        assert expected_message in message, \
            f"Expected message: {expected_message} has not been found in message: {message}"

    def should_be_message_with_price_for_added_product(self, price):
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_PRICE).text
        expected_message = "Your basket total is now " + price
        assert expected_message in message, \
            f"Expected message: {expected_message} has not been found in message: {message}"
