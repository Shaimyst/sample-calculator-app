import pytest

# this tests the multiplication function

# begin test
def test_correct_results(browserdriver):
    browserdriver.get("http://localhost:5000") 

    # enter '8 x 8 =' expected result '64'

    eight_button = browserdriver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/button")
    mult_button = browserdriver.find_element_by_xpath("/html/body/main/div/div[3]/div[2]/button")
    equal_button = browserdriver.find_element_by_xpath("/html/body/main/div/div[4]/div[1]/button")

    eight_button.click()
    mult_button.click()
    eight_button.click()
    equal_button.click()
    result = browserdriver.find_element_by_xpath("/html/body/main/div/div[1]/div").text

    #assert expected results vs actual result
    assert result == "64", "FAIL"