from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetimedemo import utility


opt=Options()
#opt.add_argument("--headless")
opt.headless=True

driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=opt)
driver.maximize_window()
driver.get("http://www.google.com")
driver.find_element(By.NAME,"q").send_keys("Deepika Padukon")
driver.get_screenshot_as_file(os.getcwd()+"/Screenshots/"+"Selenium_"+utility.current_time()+".png")


