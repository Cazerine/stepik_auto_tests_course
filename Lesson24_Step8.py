from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button2 = browser.find_element(By.ID, "book")
button2.click()
#message = browser.find_element(By.ID, "verify_message")

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
rez = calc(x)

answer = browser.find_element(By.ID, "answer")
answer.send_keys(rez)

button3 = browser.find_element(By.ID, "solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button3)
button3.click()
#assert "successful" in message.text
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()