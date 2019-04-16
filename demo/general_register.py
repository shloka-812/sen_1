from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ihelpu.herokuapp.com/")
eleUserMessage = driver.find_element_by_link_text("Register").click()

eleUserMessage = driver.find_element_by_link_text(
    "General Registeration").click()
eleUserMessage = driver.find_element_by_id("id_username")
eleUserMessage.send_keys("xyz")
eleUserMessage = driver.find_element_by_id("id_password")
eleUserMessage.send_keys("xyz")
eleUserMessage = driver.find_element_by_id("id_email")
eleUserMessage.send_keys("xyz@gmail.com")
eleUserMessage = driver.find_element_by_id("id_fname")
eleUserMessage.send_keys("def")
eleUserMessage = driver.find_element_by_id("id_lname")
eleUserMessage.send_keys("abc")
eleUserMessage = driver.find_element_by_id("id_city")
eleUserMessage.send_keys("delhi")
eleUserMessage = driver.find_element_by_id("id_dob")
eleUserMessage.send_keys("12/01/1996")
eleUserMessage = driver.find_element_by_type("submit").click()
