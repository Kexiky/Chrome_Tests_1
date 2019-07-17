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

        time.sleep(3) #ожидание для полноценной загрузки и избавления от ошибок с отсутсвием формы "Нашли предложение лучше"

        lp = driver.find_element_by_xpath('//*[@id="root"]//div[@class="flocktory-widget-overlay"]')
        lp.click()

        iframe = lp.find_element_by_tag_name('iframe')
        driver.switch_to_frame(iframe)

        driver.find_element_by_class_name('js-rules').click()
        driver.find_element_by_class_name('js-personal').click()

        for i in range(1, 3):
            driver.switch_to.window(window_name=driver.window_handles[-1])
            driver.save_screenshot(str(i) + ".png")
            time.sleep(2)
            driver.close()
        driver.switch_to.window(window_name=driver.window_handles[0])
        iframe = lp.find_element_by_tag_name('iframe')
        driver.switch_to_frame(iframe)
        time.sleep(2)
        driver.find_element_by_class_name('widget__link').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
