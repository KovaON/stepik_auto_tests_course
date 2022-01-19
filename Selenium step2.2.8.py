from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_button = browser.find_element_by_css_selector(".container .btn")
    first_button.click()
    # first_name.send_keys("Антон")
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id('input_value').text
    print(x)
    x=calc(x)
    print(x)

    input_place = browser.find_element_by_id('answer')
    input_place.send_keys(x)
    submit = browser.find_element_by_css_selector('.btn.btn-primary')
    submit.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert_text=alert_text[-17:]
    print(alert_text)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()