import random


def postcode_generator() -> str:
    """Генерирует 10-ти значный почтовый код из цифр."""
    N = 10  # Количество разрядов
    post_code = ""
    for _ in range(N):
        post_code += str(random.randint(0, 9))
    return post_code


def name_generator(post_code: str) -> str:
    """
    1) Post Code условно разбиваем на двузначные цифры (получится 5 цифр)
    2) Каждую цифру преобразовываем в букву английского алфавита по порядку от 0 до 25.
    Если цифра больше 25, то начинаем с 26 как с 0. Т.е. 0 - a, 26 - тоже a, 52 – тоже a, и т.д.
    Пример: 0001252667 = abzap
    >>> name_generator('0001252667')
    'abzap'
    >>> name_generator('26')
    'a'
    >>> name_generator('52')
    'a'
    """
    N = 2  # Длина нарезки
    name = ""
    for i in range(0, len(post_code), N):
        element = int(post_code[i: i + N])
        if element < 26:
            name += chr(element + 97)
        else:
            name += chr((element) % 26 + 97)
    return name


def choose_average_length_name(names: list[str]) -> str:
    """
    Принимает непустой список.
    Возвращает первого клиента с именем, именем, длина которого будет ближе
    к среднему арифметическому из всего списка имён.
    >>> choose_average_length_name(['Albus', 'Voldemort', 'Neville'])
    'Neville'
    >>> choose_average_length_name(['Шу', 'Шу', 'Шу', 'Шубадуба'])
    'Шу'
    >>> choose_average_length_name(['Биба', 'Боба'])
    'Биба'
    >>> choose_average_length_name([])
    ''
    """
    if not names:
        return ""
    average = sum(len(name) for name in names) // len(names)
    names_delta = [(name, abs(len(name) - average)) for name in names]
    first_avg_name = sorted(names_delta, key=lambda x: x[1])[0][0]
    return first_avg_name


def reverse_sort_table(table_data: str) -> str:
    """
    Принимает строку. Разрезает ее по переводам строк (\n).
    Фильтрует по первому слову в обратном алфавитном
    порядке на исключение первого элемента.
    Возвращает отсортированную в обратном поряде строку.
    >>> reverse_sort_table('First Last')
    'First Last'
    """
    table_data = table_data.split("\n")
    table_data_header = table_data[0]
    table_data.pop(0)
    table_data.sort(reverse=True)
    table_data.insert(0, table_data_header)
    table_data = "\n".join(table_data)
    return table_data


if __name__ == "__main__":
    import doctest

    doctest.testmod()
