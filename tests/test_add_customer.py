import allure
import pytest

from pages.add_customer_page import AddCustomerPage


@allure.epic("Тестирование создания клиента (Add Customer)")
class TestRegistrationPage:

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
    def test_registration_page_allert_text(self, driver, customer_data):

        with allure.step(f"Открытие страницы {self.link}"):
            page = AddCustomerPage(driver, self.link)
            page.open_link()

        with allure.step("Нажатие кнопки Add Customer"):
            page.click_add_customer_button()

        with allure.step("Заполнение формы создания нового клиента"):
            page.fill_registration_form(**customer_data)

        with allure.step("Нажатие кнопки Add customer в форме"):
            page.click_submit_button()

        with allure.step("Проверка содержимого текста в alert"):
            alert = driver.switch_to.alert
            alert_text = alert.text
            expected_content = "Customer added successfully with customer id"
            assert (
                expected_content in alert_text
            ), "Текст в alert отличается от отжидаемого"
