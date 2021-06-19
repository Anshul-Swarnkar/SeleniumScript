from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

opt=Options()
opt.add_argument("--headless")

driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=opt)
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(20)
driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("apple phone")
driver.find_element(By.XPATH,"//input[@value='Go']").click()
driver.find_element(By.XPATH,"//span[text()='Apple']").click()
phones=driver.find_elements(By.XPATH,"//a[@class='a-link-normal a-text-normal']//span[@class='a-size-base-plus a-color-base a-text-normal']")
prices=driver.find_elements(By.XPATH,"//span[@class='a-price-whole']")

myphone=[]
myprice=[]

for phone in phones:
    #print(phone.text)
    myphone.append(phone.text)

driver.implicitly_wait(3)

for price in prices:
    #print(price.text)
    myprice.append(price.text)

finallist=zip(myphone,myprice)

print("Part 1")

#for data in list(finallist):
#    print(data)

wb=Workbook()
wb["Sheet"].title="Apple Phone"
sh1=wb.active
sh1.append(["Name","Price"])

for x in list(finallist):
    sh1.append(x)

wb.save("FinalData.xlsx")

print("Part 2")

