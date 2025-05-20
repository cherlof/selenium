import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser",
                     default="chrome",
                     choices=["chrome", "firefox", "edge"],
                     help="Выберите браузер для запуска тестов"
                     )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")
        _driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        _driver = webdriver.Firefox(options=options)

    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--headless")
        _driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    yield _driver
    _driver.quit()
