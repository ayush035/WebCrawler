from selenium import webdriver
import time
a=input ("what you want to search")
path = "C:\DRIVERS\chromedriver.exe" 
driver = webdriver.Chrome(path)
driver.get("http://amazon.in")
search = driver.find_element_by_name("field-keywords")
search.send_keys(a)
driver.find_element_by_id("nav-search-submit-text").click()
driver.get("http://flipkart.com")
search = driver.find_element_by_name("q")
search.send_keys(a)
driver.find_element_by_class("L0Z3Pu").click()
print(driver.page_source)
time.sleep(5)



