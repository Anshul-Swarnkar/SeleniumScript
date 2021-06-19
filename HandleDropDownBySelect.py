from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\Dell\\Downloads\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.facebook.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[text()='Create New Account']").click()
time.sleep(3)

month=driver.find_element(By.NAME,"birthday_month")
monthDD=Select(month)

monthDD.select_by_index(3)
time.sleep(3)

monthDD.select_by_value("7")
time.sleep(3)

monthDD.select_by_visible_text("Oct")
time.sleep(3)
