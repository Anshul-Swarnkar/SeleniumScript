from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.thetestingworld.com/index.php?option=com_users&view=registration&Itemid=588")

driver.find_element(By.ID,"jform_name").send_keys("Anshul")

act=ActionChains(driver)
#act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys('a').perform()
time.sleep(5)

act.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys(Keys.DELETE).perform()