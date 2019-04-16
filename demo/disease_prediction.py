from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ihelpu.herokuapp.com/")

eleUserMessage = driver.find_element_by_link_text("Disease Prediction").click()
eleUserMessage = Select(driver.find_element_by_id("id_symptoms_1"))
eleUserMessage.select_by_visible_text("back_pain")
