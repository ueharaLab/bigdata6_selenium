from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
 
  
# ドライバー指定でChromeブラウザを開く
#driver = webdriver.Chrome(executable_path=r"")
driver = webdriver.Edge(executable_path=r".\edge_driver\msedgedriver.exe")
# Googleアクセス
driver.get('https://www.google.com/')
time.sleep(3)
# 検索ボックスを特定
elem = driver.find_element(By.NAME, 'q')
time.sleep(3)
# 「Selenium」と入力して、「Enter」を押す
elem.send_keys('Selenium' + Keys.RETURN)