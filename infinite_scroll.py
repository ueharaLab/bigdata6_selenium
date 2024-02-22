import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import urllib
import pandas as pd
import os
import codecs

#driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
driver = webdriver.Edge(executable_path=r".\edge_driver\msedgedriver.exe")

driver.get('https://www.yahoo.co.jp/')   
driver.maximize_window()    


while True:  
    
    #time.sleep(4)   
    #dr.find_element_by_tag_name('body').click() # クリックしないと動作しない場合もある
    #driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(4)
    
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    