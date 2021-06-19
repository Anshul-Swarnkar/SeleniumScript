from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
parentwindow=driver.current_window_handle
print("Parent Window handle ",parentwindow)
driver.find_element(By.XPATH,"//img[@alt='LinkedIn OrangeHRM group']").click()
child_window=driver.window_handles
print("Types of all windows ",type(child_window))

for child in child_window:
    print(child)
    if parentwindow!= child:
        print("Switching to new window")
        driver.switch_to.window(child)
        print("Title is ",driver.title)
        driver.find_element(By.ID,"email-or-phone").send_keys("Selenium")
        driver.close()

driver.switch_to.window(parentwindow)
print("parent window title is ",driver.title)
driver.find_element(By.ID,"txtUsername").send_keys("Admin")








