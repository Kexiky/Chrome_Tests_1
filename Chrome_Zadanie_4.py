import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # noinspection PyDeprecation
    def test_LP(self):
        driver = self.driver
        driver.get("https://msk.tele2.ru")

        #1 Вход в личный кабинет
        driver.find_element_by_class_name('login-action-new').click()
        time.sleep(3)

        log_in = driver.find_element_by_class_name(
            'iframe-top-padding'
        )

        iframe = log_in.find_element_by_tag_name('iframe')
        driver.switch_to_frame(iframe)

        driver.find_element_by_class_name(
            'payment-options-double'
        ).find_elements_by_tag_name('li')[1].click()
        time.sleep(3)

        phone = ''    #Номер пользователя
        password = ''     #Пароль пользователя

        user_phone = driver.find_element_by_id('phone-password')
        user_phone.send_keys(phone)
        user_password = driver.find_element_by_id('password-field')
        user_password.send_keys(password)
        user_password.submit()
        time.sleep(5)

        #2 Вывод баланса и остатков в консоль
        driver.find_element_by_class_name(
            'login-action-new'
        ).click()
        time.sleep(5) #ожидание полноценной загрузки
        balance = driver.find_element_by_id(
            'root'
        ).find_element_by_class_name('number')
        print('Ваш баланс составляет: ' + balance.text)

        remains = driver.find_element_by_id(
            'root'
        ).find_elements_by_class_name('rate-box-lk')

        print('Остатки тарифа: ')
        for i in range(len(remains)):
            print(remains[i].text)
        time.sleep(5)

        #3 Расходы по месяцам 2019 года
        driver.find_elements_by_class_name('box-link-advanced')[1].click()
        for i in range(12):
            time.sleep(3)
            month = driver.find_element_by_class_name(
                'sum-line'
            ).find_element_by_class_name(
                'title'
            ).text + ': ' + driver.find_element_by_class_name(
                'sum-line'
            ).find_element_by_class_name(
                'value'
            ).text
            print(month)
            try:
                driver.find_element_by_class_name('icon-left-arrow').click()
            except NoSuchElementException:
                break





    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
