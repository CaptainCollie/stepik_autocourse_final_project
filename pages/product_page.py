from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()
        # self.solve_quiz_and_get_code()
        self.should_be_success_message_with_right_book_name()
        self.should_be_right_basket_sum()

    def check_success_message_is_not_present_after_add_to_basket(self):
        self.should_be_add_to_basket_button()
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()
        # self.solve_quiz_and_get_code()
        self.should_be_success_message_with_right_book_name()

    def check_message_disappeared_after_adding_product_to_basket(self):
        self.should_be_add_to_basket_button()
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()
        # self.solve_quiz_and_get_code()
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS), "Success message is not disappeared"

    def should_see_product_in_basket_opened_from_product_page(self):
        self.go_to_basket_page()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "There is no add to basket button"

    def should_be_success_message_with_right_book_name(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESS), "There is no success alert"
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_name == self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS).text, "Wrong book name"

    def should_be_right_basket_sum(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_SUM).text == self.browser.find_element \
            (*ProductPageLocators.BOOK_PRICE).text, "Wrong book price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS), "Success message is present"
