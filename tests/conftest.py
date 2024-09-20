import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

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
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()
