#Alexa Bowman 
#MedNews Tool that can differentiate between truthful headlines vs misleading headlines

#imports 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



#webscraper (Chrome ver. 137.0.7151.122)
driver = webdriver.Chrome()

#this is where im scraping all of my medical news from
driver.get("https://www.ctvnews.ca/health/") 
driver.quit()