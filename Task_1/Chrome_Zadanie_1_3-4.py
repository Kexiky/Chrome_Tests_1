import unittest
import time
from selenium import webdriver

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
        time.sleep(4)
        price = driver.find_element_by_class_name('price').text
        name_tariff = driver.find_element_by_class_name('line').text
        price_tariffs.update({name_tariff: int(price)})
    return price_main, price_tariffs

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        moskov = "https://msk.tele2.ru"
        rostov = "https://rostov.tele2.ru"
        msk = Chek_price(driver, moskov)
        print('Москва:', moskov,
              '\nЦены на главной странице: ', msk[0],
              '\nЦены на странице тарифов: ', msk[1])
        rnd = Chek_price(driver, rostov)
        print('\nРостов-на-Дону:', rostov,
              '\nЦены на главной странице: ', rnd[0],
              '\nЦены на странице тарифов: ', rnd[1])
        #4



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()