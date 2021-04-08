#importing necessary module for Selenium Python tutorial
import pytest
from selenium import webdriver
import sys
import os
import time

#Initiating ChromeDriver for this Selenium Python tutorial
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get('https://lambdatest.github.io/sample-todo-app/')
driver.maximize_window

#Identifying Required Elements and performing necessary operation on them for Selenium Python tutorial
driver.find_element_by_name("li1").click()
driver.find_element_by_name("li2").click()

driver.find_element_by_id("addbutton").click()
time.sleep(5)

 
output_str = driver.find_element_by_name("li6").text

driver.close()