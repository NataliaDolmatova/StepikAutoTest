from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    treasure = browser.find_element_by_id('input_value')
    x = treasure.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)
    input2 = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
    input2.click()
    input3 = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
    input3.click()
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
