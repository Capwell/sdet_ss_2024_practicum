from .base_page import BasePage
from .locators import CustomerFrstNameSortPageLocators as Locators


class CustomerFrstNameSortPage(BasePage):

    def click_customers_button(self):
        self.find_element(Locators.LOCATOR_CUSTOMERS_BUTTON).click()

    def click_first_name_sort_link(self):
        self.find_element(Locators.LOCATOR_FIRST_NAME_SORT_LINK).click()

    def get_table_data(self):
        return self.get_text(Locators.LOCATOR_TABLE)
