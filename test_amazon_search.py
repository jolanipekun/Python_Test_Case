from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://www.amazon.co.uk/")
search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("shirts", Keys.ENTER)

expected_text = '"shirts"'
actual_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

assert expected_text == actual_text, f'Error, Expected text {expected_text}, but actual text {actual_text}'

driver.quit()