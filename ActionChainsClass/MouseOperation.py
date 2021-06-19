from selenium import webdriver
from selenium.webdriver.support import select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.thetestingworld.com/")
driver.maximize_window()

# left mouse click
act=ActionChains(driver)
#act.send_keys().perform()

# Right mouse click
#act.context_click().perform()

# click on perticular element
#act.click(driver.find_element(By.XPATH,"//a[text()='Login']")).perform()

#for double click
#act.double_click().perform()
#act.double_click(driver.find_element(By.XPATH,"//a[text()='Login']")).perform()

act.move_to_element(driver.find_element(By.XPATH,"//span[text()='TUTORIAL ']")).perform()