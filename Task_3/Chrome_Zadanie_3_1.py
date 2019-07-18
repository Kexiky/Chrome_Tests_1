import unittest
import time
from selenium import webdriver


def Driver_get_tele2(dr):
    dr.get("https://msk.tele2.ru/")
    dr.find_element_by_class_name('menu-action').click()
    time.sleep(2)
    return dr.find_element_by_class_name('mobile-menu-modal')


def driver_click_dir(m1_1, i):
    m1_1.find_elements_by_xpath("//*[@class='main-mobile-menu']//a")[i].click()
    return m1_1.find_elements_by_class_name('regular')


class Tele2_tasks(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_tele2(self):
        driver = self.driver

        menu_1_1 = Driver_get_tele2(driver)

        for i in range(4):
            menu_list_1 = driver_click_dir(menu_1_1, i)

            for j in range(len(menu_list_1)):
                m1 = menu_list_1[j]
                for k in range(len(m1.find_elements_by_tag_name('a'))):
                    menu_list_1_1 = menu_list_1[j].find_elements_by_tag_name('a')
                    menu_list_1_1[k].click()
                    time.sleep(3)
                    menu_1_1 = Driver_get_tele2(driver)
                    menu_list_1 = driver_click_dir(menu_1_1, i)
            menu_1_1 = Driver_get_tele2(driver)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
