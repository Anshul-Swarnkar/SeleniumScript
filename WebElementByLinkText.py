from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\Dell\\Downloads\\chromedriver.exe")
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

#Here on this URl we will try to cover Link_Text and Partial_LInk_Text selectors

#forgotpass=driver.find_element(By.LINK_TEXT,"Forgot your password?")
#forgotpass.click()

#here we will use Partial Link Text selector

forgotpass=driver.find_element(By.PARTIAL_LINK_TEXT,"Forgot your")
forgotpass.click()