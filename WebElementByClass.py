#If you are working with latest version of Selenium with Python then sure you must have got below warning find_element_by_* commands are deprecated. Please use find_element() instead. In order to fix this we will be using the By class and will use find_element() method.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\Dell\\Downloads\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

#driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
#  Instead of above code we can replace By.Name with simple name.
driver.find_element("name","txtUsername").send_keys("Admin")

#driver.find_element(By.ID,"txtPassword").send_keys("admin123")
#  Instead of above code we can replace By.ID with simple id.
driver.find_element("id","txtPassword").send_keys("admin123")

#driver.find_element(By.CLASS_NAME,"btnLogin").click()
#  Instead of above code we can replace By.CLASS_NAME with simple class name.
driver.find_element("class name","button").click()
driver.quit()



