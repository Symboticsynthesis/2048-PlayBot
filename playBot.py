import requests
import os
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(r'C:\Users\User1\Desktop\chromedriver')
browser.get('https://gabrielecirulli.github.io/2048/')
search = browser.find_element_by_css_selector('body')

for i in range(100):
    search.send_keys(Keys.RIGHT)
    search.send_keys(Keys.LEFT)
    search.send_keys(Keys.UP)
    search.send_keys(Keys.DOWN)
    search.send_keys(Keys.LEFT)
    

