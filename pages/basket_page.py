from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_basket_be_empty(self):
        self.should_be_basket_is_empty_message()
        self.should_not_items_in_basket()

    def should_be_basket_is_empty_message(self):
        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-cn": "Your basket is empty.",
        }
        f = False
        basket_is_empty_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MSG).text
        for language in languages:
            if language in basket_is_empty_text:
                f = True
        assert f, "There is no basket is empty message"

    def should_not_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"
