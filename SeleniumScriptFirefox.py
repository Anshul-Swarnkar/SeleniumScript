from selenium import webdriver

driver=webdriver.Firefox(executable_path="C:\\Users\\Dell\\Downloads\\geckodriver.exe")
driver.get("http://learn-automation.com")
titlename=driver.title
print(titlename)
print(driver.current_url)
driver.quit()

