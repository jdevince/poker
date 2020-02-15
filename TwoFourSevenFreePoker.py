import base64
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://www.247freepoker.com/'
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)
actions = ActionChains(driver)

def play():
    driver.get(url)

    wait.until(presence_of_element_located((By.ID, "game-frame")))
    driver.switch_to.frame(driver.find_element_by_id("game-frame"))

    wait.until(presence_of_element_located((By.TAG_NAME, "canvas")))
    canvas = driver.find_element_by_id("game").find_elements_by_tag_name("canvas")[1] # Second canvas element is the real one

    print("Canvas size (height, width): " + str(canvas.size['height']) + ", " + str(canvas.size['width']) + ")") # Normally 578, 639

    actions.move_to_element_with_offset(canvas, 240, 390) # Play button
    actions.click()
    actions.perform()

    actions.move_to_element_with_offset(canvas, 290, 320) # Medium difficulty button
    actions.click()
    actions.perform()

    time.sleep(10)

    canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
    canvas_png = base64.b64decode(canvas_base64)
    with open(r"canvas.png", 'wb') as f:
        f.write(canvas_png)

    print("Done")