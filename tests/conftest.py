import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser",
                     default="chrome",
                     choices=["chrome", "opera", "firefox", "edge"],
                     help="Выберете браузер для запуска тестов"
                     )



@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Фоновый режим
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        _driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_experimental_option("detach", True)
        _driver = webdriver.Firefox()
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        _driver = webdriver.Edge()
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    yield _driver

    #_driver.close()
