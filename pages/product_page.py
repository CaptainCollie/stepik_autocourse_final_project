from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()
        self.solve_quiz_and_get_code()
        self.should_be_success_message_with_right_book_name()
        self.should_be_right_basket_sum()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "There is no add to basket button"

    def should_be_success_message_with_right_book_name(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESS), "There is no success alert"
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_name == self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS).text, "Wrong book name"

    def should_be_right_basket_sum(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_SUM).text == self.browser.find_element\
            (*ProductPageLocators.BOOK_PRICE).text, "Wrong book price"

