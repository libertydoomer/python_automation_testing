import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver

@pytest.fixture
def separator():
    print('=' * 10)
    yield  'value'
    print('finished')

@pytest.fixture(scope='session')
def all_tests():
    print('Before all')
    yield
    print('After all')