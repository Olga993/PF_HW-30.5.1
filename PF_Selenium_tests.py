import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver

    driver.quit()


def test_show_all_pets(driver):
    driver.find_element(By.ID, 'email').send_keys('pycharm_pet_friends@mail.ru')
    driver.find_element(By.ID, 'pass').send_keys('12345')
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"


def test_show_my_pets(driver):
    # Вводим email, пароль, открываем главную страницу сайта
    driver.find_element(By.ID, 'email').send_keys('pycharm_pet_friends@mail.ru')
    driver.find_element(By.ID, 'pass').send_keys('12345')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    wait = WebDriverWait(driver, 5)
    assert wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), "PetFriends"))
