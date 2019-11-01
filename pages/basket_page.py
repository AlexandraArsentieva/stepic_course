from pages.base_page import BasePage
from pages.locators import BasketLocators


class BasketPage(BasePage):
    def is_empty_alert_message(self):
        empty_alert = self.browser.find_element(*BasketLocators.BASKET_EMPTY_LABEL)
        standart_message = "Your basket is empty. Continue shopping"
        assert empty_alert.text == standart_message, "Message \"{}\" no equeal {}".format(empty_alert.text, standart_message)

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_SUMMARY), "Basket has a products"