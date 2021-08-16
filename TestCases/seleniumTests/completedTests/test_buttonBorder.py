import pytest

# this test confirms buttons have a black border

def test_button_border(browserdriver):
    browserdriver.get("http://localhost:5000")

    tags = browserdriver.find_elements_by_tag_name('button')

    for t in tags:
        t.click()
        buttonBorder = t.value_of_css_property("border")
        # print(t.tag_name + " " + t.text + " has a border of " + buttonBorder)

    assert buttonBorder == "4px solid rgb(0, 0, 0)", "Border is wrong"