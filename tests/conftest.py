import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

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
    options = Options()
    options.add_argument('--disable-application-cache')
    options.add_argument('--headless')
    options.add_argument("--no-sand box")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()
