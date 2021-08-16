import pytest

# this tests if input runs outside the display box

def test_display_box_overflow(browserdriver):
    browserdriver.get("http://localhost:5000")

    # enter test data
    # Type more than 8 characters as max limit should be 8

    eight_button = browserdriver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button")

    for i in range(12):
        eight_button.click()

    # Get the typed value
    displayBox = browserdriver.find_element_by_xpath("/html/body/main/div/div[1]/div").text
    # print("Test data used:" + displayBox)
    # print("The length is:", len(displayBox))

    # assertion
    assert len(displayBox) <= 8, "Text overflows display box"