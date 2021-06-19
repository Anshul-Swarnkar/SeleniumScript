from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://www.google.com")
driver.maximize_window()
driver.find_element(By.NAME,"q").send_keys("Sood Charity Foundation")
