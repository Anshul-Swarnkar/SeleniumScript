from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element(By.NAME,"proceed").click()
alt=driver.switch_to.alert
# capture alert box
alt_text=alt.text
print("Alert Text is ",alt_text)

# accept the alert
alt.accept()
# alt.dismiss() - when you have to cancel the alert

driver.find_element(By.NAME,"login").send_keys("Selenium")