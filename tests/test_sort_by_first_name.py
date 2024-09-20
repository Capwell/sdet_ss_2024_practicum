import allure
import pytest

from .utilits import reverse_sort_table
from pages.customers_page import CustomerPageLocators


@allure.epic("Тестирование сортировки клиентов по имени (First Name)")
class TestFirstNameSort():

    link = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

    @pytest.mark.ui
    @allure.story("Проверка сортировки")
    @allure.description(
        """
        Цель: Проверить работу сортировки клиентов по (First Name)

        Предусловия:
            - Открыть браузер

        Шаги:
            - Открыть страницу https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager
            - Нажать кнопку Customers
            - Получить список клиентов
            - Отсортировать получившийся список клиентов в обратном алфавитном порядке
            - Нажать поле First Name
            - Получить новый список
            - Сравнить с отсортированным

        Ожидаемый результат:
            - При клике на First Name список клиентов сортируется в обратном алфавитном порядке
        """
    )
    def test_first_name_sort_positive(self, driver):

        with allure.step(f"Открытие страницы {self.link}"):
            page = CustomerPageLocators(driver, self.link)
            page.open_link()

        with allure.step("Нажатие кнопки Customers"):
            page.click_customers_button()

        unsorted_table = page.get_table_data()

        with allure.step("Нажатие кнопки firt_name для сортировки"):
            page.click_first_name_sort_link()

        sorted_data = page.get_table_data()

        with allure.step("Проверка работоспосбности сортировки"):
            assert reverse_sort_table(unsorted_table) == sorted_data
