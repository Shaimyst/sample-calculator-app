import pytest

# this test finds and clicks all buttons in the app

# begin test
def test_all_buttons(browserdriver):
    browserdriver.get("http://localhost:5000")
    tags = browserdriver.find_elements_by_tag_name('button')

    count = 0

    for t in tags:
        t.click()
        count += 1 # variable will increment every loop iteration of your code
        tagname = t.tag_name
        # option: print list of all buttons clicked
        # print(t.text + " is a " + t.tag_name)

    # print("There are " + str(count) + " buttons")

    # calc should have a 16 buttons have assertion report the correct amount.
    assert count == 16, "There are not 16 buttons"
    assert count > 15, "There are buttons missing"
    assert count < 17, "There are too many buttons"