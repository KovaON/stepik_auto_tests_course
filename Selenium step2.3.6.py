from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    price100 = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"),'$100'))

    button = browser.find_element_by_id('book')
    button.click()
    #
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)

    x = browser.find_element_by_id('input_value').text
    print(x)
    x=calc(x)
    print(x)

    input_place = browser.find_element_by_id('answer')
    input_place.send_keys(x)
    submit = browser.find_element_by_id('solve')
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()