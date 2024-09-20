import allure
import pytest


from .utilits import name_generator
from pages.add_customer_page import AddCustomerPage


@allure.epic("Тестирование создания клиента (Add Customer)")
class TestRegistrationPage():

    link = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

    @pytest.mark.ui
    @allure.story("Проверка содержимого текста модального окна")
    @allure.description(
        """
        Цель: проверить создание клиента после заполнения формы

        Предусловия:
            - Открыть браузер

        Шаги:
            - Открыть страницу https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager
            - Нажать кнопку Add customer
            - Корректно заполнить данные формы создания клиента

        Ожидаемый результат:
            - Появился assert с текстом Customer added successfully with customer id и номером id.
        """
    )
    @pytest.mark.parametrize("last_name, post_code", [("Иванов", "0001252667")])
    def test_registration_page_allert_text(self, driver, last_name, post_code):

        # TODO: утащить в фикстуру как то
        first_name = name_generator(post_code)

        with allure.step(f"Открытие страницы {self.link}"):
            page = AddCustomerPage(driver, self.link)
            page.open_link()

        with allure.step("Нажатие кнопки Add Customer"):
            page.click_add_customer_button()

        with allure.step("Заполнение формы создания нового клиента"):
            page.fill_registration_form(first_name, last_name, post_code)

        with allure.step("Нажатие кнопки Add customer в форме"):
            page.push_submit_button()

        with allure.step("Проверка содержимого текста в alert"):
            alert = driver.switch_to.alert
            alert_text = alert.text
            expected_content = "Customer added successfully with customer id"
            assert expected_content in alert_text, "Текст в allert отличается от отжидаемого"
