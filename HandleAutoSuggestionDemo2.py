from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.goibibo.com/")
driver.implicitly_wait(20)
driver.find_element(By.XPATH,"//input[@placeholder='From']").send_keys("Ben")
listElement=driver.find_elements(By.XPATH,"//li[contains(@id,'react-autosuggest-1-suggestion')]//div[@class='mainTxt clearfix']//span")

print("Total selections are ",len(listElement))
for ele in listElement:
    print("Total records are ",ele.text)
    if ele.text=='Bengaluru, India':
        print("Record found")
        ele.click()
        break




