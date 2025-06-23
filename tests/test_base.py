import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("currency, symbol",[(1,'€'),(2,'£'),(3,'$')])
def test_change_currency_to_dollar(driver,currency,symbol):
    driver.get(url="http://localhost:80/")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id=\"form-currency\"]/div/a"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//*[@id=\"form-currency\"]/div/ul/li[{currency}]/a"))
    )
    element.click()

    driver.refresh()
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME,'price-new'))
    )
    assert symbol in element.text
