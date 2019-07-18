import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://msk.tele2.ru/")

menu_1 = driver.find_element_by_id('root')
menu_1.find_element_by_class_name('menu-action').click()
time.sleep(2)
menu_1_1 = menu_1.find_element_by_class_name('mobile-menu-modal')

#menu_list = menu_list.find_elements_by_tag_name('a')


for i in range(0, 4):
    menu_list = menu_1_1.find_elements_by_xpath("//*[@class='main-mobile-menu']/ul/li/a")
    menu_list[i].click()
    time.sleep(2)
    menu_1_1.find_element_by_class_name('icon-left-arrow2').click()
    time.sleep(2)

'''fatfont = driver.find_elements_by_tag_name('strong')
for i in fatfont:
    print(i.id, ' ', i.text)

# fatfont1 = driver.find_element_by_tag_name('b')
'''

time.sleep(5)
driver.quit()
