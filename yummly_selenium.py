import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import urllib
import pandas as pd
import os
import codecs

#dr = webdriver.Chrome(executable_path=r'C:\Users\uhoku\AppData\Roaming\Python\Python39\Scripts\chromedriver')
#dr.get("https://www.yummly.com/recipes?q=pork&taste-pref-appended=true")
#for elem in dr.find_elements_by_xpath('//*[@class="recipe-card-img placeholder"]'):
    
    #print(elem.text)
#    print(elem.get_attribute('data-pin-url'))

# seleniumでuser agentを変える方法  
#https://tachitechi.com/change-user-agent-with-selenium/
def get_url(drvr):
    urls=[]
    for elem in drvr.find_elements_by_xpath('//*[@class="recipe-card-img placeholder"]'):
        
        #print(elem.text)
        url=elem.get_attribute('data-pin-url')   
        urls.append([search_word,url])
        print(url)
    recipe_df = pd.DataFrame(urls,columns=['key_word','url'])
    
    if os.path.isfile('./dataset/yummly_url.csv'):

        with codecs.open("./dataset/yummly_url.csv", "a", "ms932", "ignore") as f: 
            recipe_df.to_csv(f, index=False, encoding="ms932", mode='a', header=False)
    else: 
        with codecs.open("./dataset/yummly_url.csv", "w", "ms932", "ignore") as f: 
            #header=Trueで、見出しを書き出す
            recipe_df.to_csv(f, index=False, encoding="ms932", mode='w', header=True)
    
                    
search_word = input('key word ? ')
searchWord_encode = urllib.parse.quote(search_word)
dr = webdriver.Chrome(executable_path=r'C:\Users\uhoku\AppData\Roaming\Python\Python39\Scripts\chromedriver')
dr.get("https://www.yummly.com/recipes?q={}&taste-pref-appended=true".format(searchWord_encode))    
dr.maximize_window()    


# ブラウザが開いたら、まずクリックすること。これでスクロールできるようになる。
#  dr.find_element_by_tag_name('body').click() # のように自動クリックを使うと広告バナーを誤ってクリックして別のページに飛んでしまうので使えない
while True:  
    
    time.sleep(4)   
    #dr.find_element_by_tag_name('body').click() # クリックしないと動作しない場合もある
    dr.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(4)
    
    dr.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    get_url(dr)