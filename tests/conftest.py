import pytest
from selenium import webdriver

from .utilits import name_generator


@pytest.fixture
def customer_data(last_name="Иванов", post_code="0001252667"):
    first_name = name_generator(post_code)
    return {
        "first_name": first_name,
        "last_name": last_name,
        "post_code": post_code,
    }


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
