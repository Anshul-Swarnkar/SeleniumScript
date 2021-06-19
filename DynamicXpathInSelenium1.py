#Syntax of Dynamic Xpath
#//input[@name,id,class etc='value']

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\Dell\\Downloads\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//input[@value='LOGIN']").click()

print("Current URL After Login ",driver.current_url)
assert "dashboard" in driver.current_url

driver.find_element(By.XPATH,"//a[contains(text(),'Welcome')]").click()
time.sleep(3)

driver.find_element(By.XPATH,"//a[contains(text(),'Logout')]").click()

print("After logout",driver.current_url)

assert "login" in driver.current_url

driver.quit()



