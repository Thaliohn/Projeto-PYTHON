from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.youtube.com')

driver.find_element(By.XPATH, '//*[@id="search"]').click()