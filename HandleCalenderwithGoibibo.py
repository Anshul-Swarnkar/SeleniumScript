from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.goibibo.com/")
driver.implicitly_wait(20)
driver.find_element(By.ID,"departureCalendar").click()
datelist=driver.find_elements(By.XPATH,"//div[@class='DayPicker-Day']//div")

for dateElement in datelist:
    date=dateElement.text
    print(date)
    if date=='14':
        dateElement.click()
        print("Departure Date Is ",date)
        break