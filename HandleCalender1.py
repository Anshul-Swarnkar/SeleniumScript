from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.implicitly_wait(20)
driver.find_element(By.ID,"datepicker").click()
#driver.find_element(By.XPATH,"//a[text()='25']").click()
dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//a")

for dateElement in dates:
    date=dateElement.text
    print(date)
    if date=='25':
        dateElement.click()
        break






