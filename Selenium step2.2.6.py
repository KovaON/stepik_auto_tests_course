from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector(".form-group [name='firstname']")
    first_name.send_keys("Антон")

    last_name = browser.find_element_by_css_selector(".form-group [name='lastname']")
    last_name.send_keys("Кокоджамбо")

    email = browser.find_element_by_css_selector(".form-group [name='email']")
    email.send_keys("kuku@ya.ru")

    element_input = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element_input.send_keys(file_path)
    print(file_path)

    submit = browser.find_element_by_css_selector('.btn.btn-primary')
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()