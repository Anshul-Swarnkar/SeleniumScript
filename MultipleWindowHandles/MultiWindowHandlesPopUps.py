from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.naukri.com/")
driver.maximize_window()

mainwin=""

Allwindow=driver.window_handles
for win in Allwindow:
    driver.switch_to.window(win)
    #print(driver.current_url)
    if(driver.current_url=="https://www.naukri.com/"):
        mainwin==win
    else:
        driver.close()

driver.switch_to.window(mainwin)
print(driver.current_url)