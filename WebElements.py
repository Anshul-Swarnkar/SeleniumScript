from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\Dell\\Downloads\\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

username=driver.find_element_by_name("txtUsername")
username.send_keys("Admin")

EnableStatus=username.is_enabled()
print(EnableStatus)

DisplayStatus=username.is_displayed()
print(DisplayStatus)

username.clear()

arrtdata=username.get_attribute("type")
print(arrtdata)

fontvalue=username.value_of_css_property("font-size")
print(fontvalue)

password=driver.find_element_by_name("txtPassword")
password.send_keys("admin123")

loginbutton=driver.find_element_by_id("btnLogin")
loginbutton.click()

driver.quit()

#if you don't need to store username, password and login button in variable you can simply put it one line of code and that you can see in next python file which is WebElements2.


