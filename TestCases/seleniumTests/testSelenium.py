import os
from selenium import webdriver

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("http://dailymotion.com")
driver.quit()

# when 10 8's are entered, they overflow the display box
# when 20 8's are entered, they show an incorrect amount
# when 24 8's are entered, it shows "infinity"