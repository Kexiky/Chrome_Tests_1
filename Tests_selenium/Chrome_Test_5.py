from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

current_url = driver.current_url
new_window_url = driver.find_element_by_link_text("Open new window").get_attribute("href")
driver.get(new_window_url)

# ... тестируем на новом сайте

driver.find_element_by_name("name").send_keys("sometext")
driver.get(current_url)  # Назад