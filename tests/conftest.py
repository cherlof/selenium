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
        options.add_argument("--headless")  # Фоновый режим
        options.add_argument("--no-sandbox")  # Отключает sandbox (важно для CI/CD)
        options.add_argument("--disable-dev-shm-usage")  # Исправляет ошибки shared memory
        options.add_argument("--disable-gpu")  # Отключает GPU
        options.add_argument("--remote-debugging-port=9222")  # Устраняет сбои DevTools
        _driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        _driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--headless")
        _driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    yield _driver
    _driver.quit()
