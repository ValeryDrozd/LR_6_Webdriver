from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
site_address = 'https://rozetka.com.ua/'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(site_address)
search_bar_name = 'search'
search_bar = driver.find_element_by_name(search_bar_name)
search_bar.clear()
search_text = 'Iphone 12'
search_bar.send_keys(search_text)
search_bar.send_keys(Keys.RETURN)
time.sleep(3)
wanted_class_name = 'goods-tile__picture'
found_elements = driver.find_elements_by_class_name(wanted_class_name)
assert len(found_elements)>0
print(len(found_elements))
driver.close()
