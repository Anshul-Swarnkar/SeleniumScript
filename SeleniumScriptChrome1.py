from selenium import webdriver

#from selenium.webdriver.chrome.service import Service # we have to import it we are getting any warning error for below executable path
#s=Service(""C:\\Users\\Dell\\Downloads\\chromedriver.exe")
#driver=webdriver.Chrome(service=s)


driver=webdriver.Chrome(executable_path="C:\\Users\\Dell\\Downloads\\chromedriver.exe")
print(type(driver))

#To Open the browser
driver.get("http://www.google.com")
#To return the title of the web page
titlename=driver.title
print(titlename)
#try assert method
assert "Google" in titlename
#To close the current browser window
driver.quit()
#To know the what kind of quit() method is
print(driver.quit) # here once you run the file you can get that this is a bound method of webdriver.





