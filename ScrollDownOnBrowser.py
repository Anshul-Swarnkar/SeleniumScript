from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.thetestingworld.com/testings/")
driver.maximize_window()
time.sleep(2)
driver.execute_script("window.scrollTo(0,400)")