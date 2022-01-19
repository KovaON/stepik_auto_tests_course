from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    x = int(num1)+int(num2)
    print(x)
    select = Select(browser.find_element_by_css_selector('select.custom-select'))
    select.select_by_value(str(x))

    # answer = browser.find_element_by_id('answer')
    # answer.send_keys(x)


    submit = browser.find_element_by_css_selector('button.btn-default')
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()