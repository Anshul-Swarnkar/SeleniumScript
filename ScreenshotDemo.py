from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetimedemo import utility
import os

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://www.google.com")
driver.get_screenshot_as_file(os.getcwd()+"/Screenshots/"+"Selenium_"+utility.current_time()+".png")

driver.get("http://www.facebook.com")
driver.get_screenshot_as_file(os.getcwd()+"/Screenshots/"+"Selenium_"+utility.current_time()+".png")
driver.get_scree


driver.quit()