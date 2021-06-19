from selenium import webdriver

driver=webdriver.Edge(executable_path="C:\\Users\\Dell\\Downloads\\msedgedriver.exe")
driver.get("http://www.google.com")
titlename=driver.title
print(titlename)
assert "Google" in titlename
driver.quit()