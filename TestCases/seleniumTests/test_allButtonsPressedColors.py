import os
from selenium import webdriver
import pytest
import time

# this test is to press all buttons and make sure they change color

#preconditions

# open virtual environment in terminal with source env/bin/activate
# spin up in terminal with make dev
# spin down with control c

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost:5000")

# check their css

# compare css after pressed

# press all buttons
# clicking loop
like = driver.find_elements_by_class_name("svelte-1wpgx6i")
for x in range(0,len(like)):
    if like[x].is_displayed():
        like[x].click()

# get CSS values
WebElement body=driver.findElement(By.tagName("body"));
    WebElement button=driver.findElement(By.id("slide"));
    System.out.println("Body bg-color Before Click: "+body.getCssValue("background-color"));
    System.out.println("Button bg-color Before Click: "+button.getCssValue("color"));
    System.out.println();
    button.click();
    System.out.println("Body bg-color After Click: "+body.getCssValue("background-color"));
    System.out.println("Button bg-color After Click: "+button.getCssValue("color"));

# only return fails

# close window