from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\Dell\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//*[text()='Create New Account']").click()
#time.sleep(3)
driver.find_element(By.NAME,"firstname").send_keys("Manohar")
driver.find_element(By.NAME,"lastname").send_keys("Kokare")
driver.find_element(By.NAME,"reg_email__").send_keys("manohar.kokare@gmail.com")
driver.find_element(By.NAME,"reg_email_confirmation__").send_keys("manohar.kokare@gmail.com")
driver.find_element(By.NAME,"reg_passwd__").send_keys("12345")

day=Select(driver.find_element(By.XPATH,"//select[@title='Day']"))
day.select_by_visible_text("16")

month=Select(driver.find_element(By.XPATH,"//select[@name='birthday_month']"))
month.select_by_visible_text("Sep")

year=Select(driver.find_element(By.XPATH,"//select[@name='birthday_year']"))
year.select_by_visible_text("1990")

driver.find_element(By.XPATH,"//label[text()='Male']").click()
driver.find_element(By.XPATH,"//button[text()='Sign Up']").click()



