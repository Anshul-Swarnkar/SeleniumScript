from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\Dell\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com/")

driver.find_element(By.XPATH,"//a[text()='Create New Account']").click()
time.sleep(3)

month=driver.find_element(By.ID,"month")
monthDD=Select(month)
monthlist=monthDD.options

firstItem=monthDD.first_selected_option
print("First option is ",firstItem.text)
assert "May"==firstItem.text

print(len(monthlist))
assert 13==len(monthlist)

for ele in monthlist:
    print("Value is ",ele.text)
    if ele.text=="Nov":
        ele.click()
        break




