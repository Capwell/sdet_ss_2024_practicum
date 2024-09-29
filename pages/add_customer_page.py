from .base_page import BasePage
from .locators import AddCustomerPageLocators as Locators


class AddCustomerPage(BasePage):

    def click_add_customer_button(self):
        self.find_element(Locators.LOCATOR_ADD_CUSTOMER_BUTTON).click()

    def set_first_name(self, input):
        self.find_element(Locators.LOCATOR_FIRST_NAME_FIELD).send_keys(input)

    def set_last_name(self, input):
        self.find_element(Locators.LOCATOR_LAST_NAME_FIELD).send_keys(input)

    def set_post_code(self, input):
        self.find_element(Locators.LOCATOR_POST_CODE_FIELD).send_keys(input)

    def click_submit_button(self):
        self.find_element(Locators.LOCATOR_ADD_SUBMIT_CUSTOMER_BUTTON).click()

    def fill_registration_form(self, first_name, last_name, post_code):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_post_code(post_code)
