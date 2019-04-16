from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ihelpu.herokuapp.com/")
eleUserMessage = driver.find_element_by_link_text("Register").click()

eleUserMessage = driver.find_element_by_link_text(
    "Pharmacy Registration").click()
eleUserMessage = driver.find_element_by_name("username")
eleUserMessage.send_keys("xyz")
