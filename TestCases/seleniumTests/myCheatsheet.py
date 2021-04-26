# find element attributes with
#print(dir(displayBox))

#save screenshot
# driver.save_screenshot('/Users/jessicasadler/git/sample-calculator-app/TestCases/seleniumTests/screenshots/screenshot_displayBoxDoesntOverflow.png')

# time.sleep(3)
# don't use sleep, instead use wait
# timeout = 10
 
# try:
#     element_present = EC.presence_of_element_located((By.LINK_TEXT, 'Sitemap'))
#     WebDriverWait(driver, timeout).until(element_present)
# except TimeoutException:
#     print("Timed out while waiting for page to load")

# implicit wait
# driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);

#close browser
# driver.quit()