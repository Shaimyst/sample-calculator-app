import os
from selenium import webdriver

# a starter test to make sure selenium and chromedriver are working

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("http://dailymotion.com")
driver.quit()