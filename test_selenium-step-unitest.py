import unittest
from selenium import webdriver

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector(".first_block .first")
        first_name.send_keys("Майкл")

        second_name = browser.find_element_by_css_selector(".first_block .second")
        second_name.send_keys("Кокоджамбо")

        email = browser.find_element_by_css_selector(".first_block .third")
        email.send_keys("ukachaka@ya.ru")

        phone = browser.find_element_by_css_selector(".second_block .first")
        phone.send_keys('89995551234')

        adres = browser.find_element_by_css_selector(".second_block .second")
        adres.send_keys('moscow')

        button = browser.find_element_by_css_selector('.btn.btn-default')
        button.click()

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # Считываем результат и обозначаем ожидаемый результат
        result = browser.find_element_by_css_selector('.container ').text
        expect = 'Congratulations! You have successfully registered!'
        # Сравниваем ожидание и результат
        self.assertEqual(expect, result, "Результат не соответствует ожиданию")
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector(".first_block .first")
        first_name.send_keys("Майкл")

        email = browser.find_element_by_css_selector(".first_block .third")
        email.send_keys("ukachaka@ya.ru")

        phone = browser.find_element_by_css_selector(".second_block .first")
        phone.send_keys('89995551234')

        adres = browser.find_element_by_css_selector(".second_block .second")
        adres.send_keys('moscow')

        button = browser.find_element_by_css_selector('.btn.btn-default')
        button.click()

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # Считываем результат и обозначаем ожидаемый результат
        result = browser.find_element_by_css_selector('.container ').text
        expect = 'Congratulations! You have successfully registered!'
        # Сравниваем ожидание и результат
        self.assertEqual(expect, result, "Результат не соответствует ожиданию")
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()