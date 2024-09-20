from selenium.webdriver.support.wait import WebDriverWait  # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type: ignore


class BasePage:

    def __init__(self, driver, link):
        self.driver = driver
        self.link = link

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_texts(self, locator):
        return self.find_elements(locator)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def set_input(self, locator, input):
        element = self.find_element(locator)
        element.send_keys(input)
        return element

    def find_element(self, locator, max_time_await=10):
        return WebDriverWait(self.driver, max_time_await).until(
                EC.presence_of_element_located(locator),
                message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, max_time_await=10):
        return WebDriverWait(self.driver, max_time_await).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    def open_link(self):
        return self.driver.get(self.link)
