# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
#
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.qa-practice.com/elements/button/simple')
# click_button = driver.find_element(By.ID, 'submit-id-submit')
# click_button.click()

# click_button2 = driver.find_element(By.CLASS_NAME, 'btn-primary')
# click_button2.click()

# click_button3 = driver.find_element(By.CSS_SELECTOR, 'input[class="btn btn-primary"]')
# click_button3.click()

# link = driver.find_element(By.LINK_TEXT, 'Contact')
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# link.click()

# click_button4 = driver.find_element(By.XPATH, '//input[@class="btn btn-primary"]')
# click_button4.click()
#
# sleep(5)

def test_one():
    assert 1 == 1
