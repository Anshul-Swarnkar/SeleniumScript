from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials")
driver.maximize_window()
driver.find_element(By.XPATH,"//img[@alt='OrangeHRM on Facebook']").click()

alltab=driver.window_handles
#print(alltab)

for tab in alltab:
    driver.switch_to.window(tab)
    if(driver.current_url=="https://www.facebook.com/OrangeHRM"):
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        driver.quit()

