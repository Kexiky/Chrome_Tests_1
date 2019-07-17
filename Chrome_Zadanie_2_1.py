import unittest
import time
from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # noinspection PyDeprecation
    def test_LP(self):
        driver = self.driver
        driver.get("https://msk.tele2.ru")
        time.sleep(3)  # ожидание для полноценной загрузки и избавления от ошибок с отсутсвием формы "Нашли предложение лучше"

        lp = driver.find_element_by_xpath('//*[@id="root"]//div[@class="flocktory-widget-overlay"]')
        lp.click()

        iframe = lp.find_element_by_tag_name('iframe')
        driver.switch_to_frame(iframe) #document

        user_phone = driver.find_element_by_id('tel')
        user_phone.send_keys('4505326149')

        user_name = driver.find_element_by_id('name')
        user_name.send_keys('Don Quixote')

        time.sleep(5)
        driver.find_element_by_class_name('widget__link').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
