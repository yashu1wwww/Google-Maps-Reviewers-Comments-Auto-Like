from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:9222")
driver = webdriver.Chrome(options=option)

time.sleep(2)

driver.get("https://www.google.com/maps/@12.9531904,77.6142848,12z?entry=ttu")

time.sleep(3)

search_box = driver.find_element_by_name("q")
search_box.send_keys("Sydney Airport (SYD), Mascot NSW, Australia") #replace with which you want like reviewers comment..
search_box.send_keys(Keys.RETURN)
    
time.sleep(7)

driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div:nth-child(3) > div > div > button:nth-child(2) > div.LRkQ2 > div.Gpq6kf.fontTitleSmall").click() #click on reviews button

time.sleep(6)

like_buttons = driver.find_elements_by_class_name("GBkF3d ")

# Click on each like button
for button in like_buttons:
    button.click()

time.sleep(50)
