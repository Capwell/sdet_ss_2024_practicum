from .base_page import BasePage
from .locators import CustomerPageLocators as Locators


class CustomerPageLocators(BasePage):

    def click_customers_button(self):
        self.click(Locators.LOCATOR_CUSTOMERS_BUTTON)

    def click_first_name_sort_link(self):
        self.click(Locators.LOCATOR_FIRST_NAME_SORT_LINK)

    def get_table_data(self):
        return self.get_text(Locators.LOCATOR_TABLE)

    def get_table_first_name(self):
        return self.find_elements(Locators.LOCATOR_FIRST_NAME_FIELD)

    def click_delete_customer_by_first_name(self, first_name):
        self.click(Locators.locator_del_button(self, first_name))
