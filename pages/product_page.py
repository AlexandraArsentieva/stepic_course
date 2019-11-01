from pages.base_page import BasePage
from pages.locators import ProductPageSelectors


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageSelectors.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def is_succeses_alert_present(self):
        succesess_alert = self.browser.find_element(*ProductPageSelectors.SUCCESES_ALERT)
        reference_alert = self.get_product_name() + " has been added to your basket."
        assert succesess_alert.text == reference_alert, \
            "Succesess alert \"{}\" not equal reference \"{}\"".format(succesess_alert.text, reference_alert)

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageSelectors.PRODUCT_NAME)
        return product_name.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageSelectors.PRODUCT_PRICE)
        return product_price.text
