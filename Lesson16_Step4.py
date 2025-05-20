from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By. XPATH, '//input[@class="form-control first" and @required=""]')
    first_name.send_keys("Test")
    last_name = browser.find_element(By. XPATH, '//input[@class="form-control second" and @required=""]')
    last_name.send_keys("Test")
    email = browser.find_element(By. XPATH, '//input[@class="form-control third" and @required=""]')
    email.send_keys("Test")


    # Отправляем заполненную форму
    button = browser.find_element(By. CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text_elt = browser.find_element(By. TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()