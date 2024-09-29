import allure
import pytest

from utilits import choose_average_length_name
from pages.delete_customers_page import DeleteCustomerPage


@allure.epic(
    "Удаление клиента с длиной имени, близкой с среднеарифметическому в списке клиентов"
)
class TestDeleteByName:

    link = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

    @pytest.mark.ui
    @allure.story("Проверить удаление клиентов по имени")
    @allure.description(
        """
        Цель: Проверить удаление клиентов по имени

        Предусловия:
            - Открыть браузер

        Шаги:
            - Открыть страницу https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager
            - Нажать кнопку Customers
            - Получить список имён клиентов
            - Определить клиента с длиной имени, близкой к среднему в списке клиентов
            - Нажать кнопку delete, соответсвую ему
            - Убедиться, что клиент с выбранным именем исчез из списка

        Ожидаемый результат:
            - При клике на кнопку Delete клиент усчезает из списка
        """
    )
    def test_delete_customer_with_name_length_closest_to_average(self, driver):

        with allure.step(f"Открытие страницы {self.link}"):
            page = DeleteCustomerPage(driver, self.link)
            page.open_link()

        with allure.step("Нажатие кнопки Customers"):
            page.click_customers_button()

        with allure.step("Получение списка customers first_name"):
            names = page.get_table_first_name()
            names_lst_before_delete = [i.text for i in names]

        with allure.step("Определение имени для удаление"):
            name_to_delete = choose_average_length_name(names_lst_before_delete)

        with allure.step(f"Удаление {name_to_delete} из списка customers"):
            page.click_delete_customer_by_first_name(name_to_delete)

        names = page.get_table_first_name()
        names_lst_after_delete = [i.text for i in names]
        delta = list(set(names_lst_after_delete) ^ set(names_lst_before_delete))

        with allure.step("Проверка удаления {name_to_delete} из списка customers"):
            assert delta == [name_to_delete], "Удалено неправильное имя"
