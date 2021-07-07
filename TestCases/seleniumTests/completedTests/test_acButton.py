import constants as c
import pytest

# this test confirms AC button clears the display box

def test_ac_button(browserdriver):
    browserdriver.get("http://localhost:5000")

    # enter test data
    eight_button = browserdriver.find_element_by_xpath(c.EIGHT_BTN_XPATH)
    ac_button = browserdriver.find_element_by_xpath(c.AC_BTN_XPATH)

    for i in range(3):
        eight_button.click()

    # Get the typed value
    display1 = browserdriver.find_element_by_xpath(c.DISPLAY_BOX_XPATH).text

    # press AC button
    ac_button.click()

    # Get the typed value
    display2 = browserdriver.find_element_by_xpath(c.DISPLAY_BOX_XPATH).text

    # return what is displayed
    # print("Test data entered: " + display1)
    # print("Data shown after clicking AC button: " + display2)

    # assert display is 0
    assert display2 == str(0), "Display box did not clear!"