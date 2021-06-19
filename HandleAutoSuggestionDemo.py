from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-autocomplete-feature-in.html")
driver.implicitly_wait(20)
driver.find_element(By.ID,"tags").send_keys("S")
listElements=driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']//div")
print("Total Suggestions are ",len(listElements))
for ele in listElements:
    print("Suggestion are ",ele.text)
    if ele.text=="Selenium":
        print("Record found")
        ele.click()
        break

