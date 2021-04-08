import os
from selenium import webdriver
import pytest
import time

# open virtual environment in terminal with source env/bin/activate
# spin up in terminal with make dev
# spin down with control c

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost:5000")


testScenario = "insert title of test"
preconditions = """
- list any preconditions
- what needs to be done for anyone to be able to run this test?
- make this fool proof, include websites, commands, etc. 
"""

test template text
testText = ["Test Scenario:"] print(testScenario)

Pre conditions: print(preconditions)


print(testText)

#print which buttons were pressed

#keep browser open for 5 seconds


#save screenshot

#close browser

#assert expected results vs actual result

#create test results document
#print test description and results
#run in terminal to create and print txt file
#python test_correctResults.py python &> results_correctResults.txt 