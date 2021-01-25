#!/usr/bin python
# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random

driver = webdriver.Firefox()
driver.get("https://www.tvaplus.ca/star-academie/vote")

girls = ["sa-0001","sa-0002","sa-0003","sa-0004","sa-0004","sa-0004","sa-0005"] #Jeni is sa-0004
guys = ["sa-0006","sa-0007","sa-0008","sa-0009","sa-0010"]

randGirl = random.choice(girls)
print("Voting for: {}".format(randGirl))
randGuy = random.choice(guys)
print("Voting for: {}".format(randGuy))

inputList = driver.find_elements(By.XPATH, "//input")
girlInput = ""
guyInput = ""
voteInput = ""

for inputBtn in inputList:
	if randGirl == inputBtn.get_attribute("data-value"):
		girlInput = inputBtn
	elif randGuy == inputBtn.get_attribute("data-value"):
		guyInput = inputBtn
	elif "Envoyer" == inputBtn.get_attribute("value"):
		voteInput = inputBtn


driver.execute_script("arguments[0].scrollIntoView();", girlInput)
girlInput.click()

driver.execute_script("arguments[0].scrollIntoView();", guyInput)
guyInput.click()

driver.execute_script("arguments[0].scrollIntoView();", voteInput)
voteInput.click()
