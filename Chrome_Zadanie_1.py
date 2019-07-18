import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def Chek_price(driver, adress):
    driver.get(adress)
    tariffs = driver.find_element_by_class_name(
        'ssc-tariffs-container'
    ).find_elements_by_class_name('swiper-slide')
    len_tariffs = len(tariffs)
    price_main = {}
    price_tariffs = {}
    for i in range(len_tariffs):
        price = tariffs[i].find_element_by_class_name('price').text
        name_tariff = tariffs[i].find_element_by_class_name('tariff-title').text
        price_main.update({name_tariff: int(price)})
        driver.find_element_by_class_name("swiper-arrow-next").click()

    for k in range(len_tariffs):
        driver.get(adress)
        for j in range(k):
            driver.find_element_by_class_name("swiper-arrow-next").click()
        driver.find_elements_by_class_name('swiper-slide')[k].click()
        time.sleep(3)
        price = driver.find_element_by_class_name('price').text
        name_tariff = driver.find_element_by_class_name('line').text
        price_tariffs.update({name_tariff: int(price)})
    return price_main, price_tariffs

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver

        #1 Жирный шрифт
        '''driver.get("https://msk.tele2.ru")
        driver.find_element_by_class_name('ssc-tariff-swipe').click()
        time.sleep(3)
        fatfont = driver.find_elements_by_tag_name('strong')
        print("Жирный шрифт:")
        for i in range(len(fatfont)):
            print(fatfont[i].text)'''

        #2 ХИТ продаж
        '''driver.get("https://msk.tele2.ru")
        tariffs = driver.find_element_by_class_name(
            'ssc-tariffs-container'
        ).find_elements_by_class_name('swiper-slide')
        for i in range(len(tariffs)):
            try:
                tariffs[i].find_element_by_class_name('hit-image')
                flag = True
            except NoSuchElementException:
                flag = False
            name_tariff = tariffs[i].find_element_by_class_name('tariff-title').text
            if flag:
                print('Тариф ' + name_tariff + ' - ХИТ продаж')
            else:
                print('Тариф ' + name_tariff + ' - не ХИТ продаж')
            driver.find_element_by_class_name("swiper-arrow-next").click()'''




    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()