from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

#driver=webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)

driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32 (1)\\chromedriver.exe",chrome_options=chrome_options)

driver.get('https://www.google.com')