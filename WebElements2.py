from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\Dell\\Downloads\\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

driver.find_element_by_name("txtUsername").send_keys("Admin")

driver.find_element_by_name("txtPassword").send_keys("admin123")

driver.find_element_by_id("btnLogin").click()

driver.quit()




