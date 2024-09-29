import logging

from .base_page import BasePage
from .locators import CustomerDeletePageLocators as Locators

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class DeleteCustomerPage(BasePage):

    def click_customers_button(self):
        self.find_element(Locators.LOCATOR_CUSTOMERS_BUTTON).click()

    def get_table_first_name(self):
        return self.find_elements(Locators.LOCATOR_FIRST_NAME_FIELD)

    def click_delete_customer_by_first_name(self, first_name):
        self.find_element(Locators.locator_del_button(self, first_name)).click()
