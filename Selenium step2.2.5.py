from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector(".form-group [name='firstname]")
    x = calc(num1)
    print(x)

    answer = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(x)

    check_box = browser.find_element_by_id('robotCheckbox')
    #browser.execute_script("return arguments[0].scrollIntoView(true);", check_box)
    check_box.click()

    radio_box = browser.find_element_by_id('robotsRule')
    #browser.execute_script("return arguments[0].scrollIntoView(true);", radio_box)
    radio_box.click()

    submit = browser.find_element_by_css_selector('.btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()