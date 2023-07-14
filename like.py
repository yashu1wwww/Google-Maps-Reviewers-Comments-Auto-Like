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
option.add_experimental_option("debuggerAddress","localhost:8080")
driver = webdriver.Chrome(options=option)

time.sleep(2)

driver.get("https://www.google.com/maps/@12.9531904,77.6142848,12z?entry=ttu")

time.sleep(3)

search_box = driver.find_element_by_name("q")
search_box.send_keys("google") #replace with which you want like reviewers comment
search_box.send_keys(Keys.RETURN)
    
time.sleep(7)

driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div:nth-child(3) > div > div > button:nth-child(2) > div.LRkQ2 > div.Gpq6kf.fontTitleSmall").click() #click on reviews button

time.sleep(6)

#its only like the starting 8 reviewers like button

driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[8]/div[1]/div/div/div[4]/div[4]/button[1]').click() #1st like

time.sleep(3)

driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[8]/div[4]/div/div/div[4]/div[4]/button[1]').click() #2nd

time.sleep(3)

driver.find_element(By.XPATH, 'html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[8]/div[7]/div/div/div[4]/div[4]/button[1]').click() #3rd

time.sleep(3)

driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[8]/div[10]/div/div/div[4]/div[4]/button[1]').click() #4th

time.sleep(3)
    
driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[8]/div[13]/div/div/div[4]/div[4]/button[1]').click() #5th
    
time.sleep(3)
    
driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[8]/div[16]/div/div/div[4]/div[4]/button[1]').click() #6th
   
time.sleep(3)
    
driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[8]/div[19]/div/div/div[4]/div[4]/button[1]').click() #7th

time.sleep(3)
    
driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[8]/div[22]/div/div/div[4]/div[4]/button[1]').click() #8th
     
time.sleep(5) 





