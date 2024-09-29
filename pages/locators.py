from selenium.webdriver.common.by import By  # type: ignore


class AddCustomerPageLocators:

    LOCATOR_ADD_CUSTOMER_BUTTON = (By.XPATH, "//*[@ng-class='btnClass1']")

    LOCATOR_FIRST_NAME_FIELD = (By.XPATH, "//*[@ng-model='fName']")
    LOCATOR_LAST_NAME_FIELD = (By.XPATH, "//*[@ng-model='lName']")
    LOCATOR_POST_CODE_FIELD = (By.XPATH, "//*[@ng-model='postCd']")

    LOCATOR_ADD_SUBMIT_CUSTOMER_BUTTON = (By.XPATH, "//*[@type='submit']")


class CustomerPageLocators:

    LOCATOR_CUSTOMERS_BUTTON = (By.XPATH, "//*[@ng-class='btnClass3']")


class CustomerFrstNameSortPageLocators(CustomerPageLocators):

    LOCATOR_FIRST_NAME_SORT_LINK = (By.XPATH, "//*[contains(@ng-click, 'fName')]")

    LOCATOR_TABLE = (By.XPATH, "//*[contains(@class, 'table')]")


class CustomerDeletePageLocators(CustomerPageLocators):

    LOCATOR_FIRST_NAME_FIELD = (By.XPATH, "//tbody/tr/td[1]")

    def locator_del_button(self, first_name):
        return (
            By.XPATH,
            f"//tbody/tr/td[1][text()='{first_name}']/..//button[text()='Delete']",
        )
