from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def is_succeses_alert_present(self):
        success_alert = self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT)
        reference_alert = self.get_product_name() + " has been added to your basket."
        assert success_alert.text == reference_alert, \
            "Success alert \"{}\" not equal reference \"{}\"".format(success_alert.text, reference_alert)

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT), "Success message is not disappeared"