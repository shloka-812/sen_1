from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ihelpu.herokuapp.com/")


eleUserMessage = driver.find_element_by_link_text("Login").click()
eleUserMessage = driver.find_element_by_name("username")
eleUserMessage.send_keys("xyz")
eleUserMessage = driver.find_element_by_name("password")
eleUserMessage.send_keys("xyz")
