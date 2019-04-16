from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ihelpu.herokuapp.com/")

eleUserMessage = driver.find_element_by_link_text("View Outbreaks").click()

"""eleUserMessage = driver.find_element_by_link_text("General Registeration").click()"""
"""eleUserMessage = Select(driver.find_element_by_id("disease_name"))
eleUserMessage.select_by_visible_text("back_pain")"""


eleUserMessage = driver.find_element_by_id("id_from_date")
eleUserMessage.send_keys("12/05/2015")
"""eleUserMessage = driver.find_element_by_name("password")
eleUserMessage.send_keys("apol")"""
"""eleUserMessage = driver.find_element_by_name("Login").click()"""
"""eleShowMsgBtn = driver.find_element_by_css_selector('#get-input > .btn')
eleShowMsgBtn.click()

eleYourMsg = driver.find_element_by_id("display")
assert "Test Python" in eleYourMsg.text
driver.close()"""
