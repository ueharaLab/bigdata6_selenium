
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import lxml
import lxml.html


driver = webdriver.Edge(executable_path=r".\edge_driver\msedgedriver.exe")


driver.get('https://4travel.jp/')
time.sleep(3)


#<a href="https://4travel.jp/domestic/day/tips/" title="国内のクチコミ">クチコミ</a>

#トップページの国内旅行のクチコミのリンクをseleniumuでクリックするには、例によって find_elementメソッド
#を使ってカーソルを移動する必要がある。
#htmlソースを見ると、title='国内のクチコミ'が手がかりだが、これをパラメータに指定することができない
#（find_element( by.TITLE....) は存在しない）。この場合は、xpathを使う。
# 
elem = driver.find_element(By.XPATH,"//a[@title='国内のクチコミ']")
elem.click()

#移動したページ上で　html = driver.page_source　と記述すると、htmlソースを取り込める
#参考サイト
#https://office54.net/python/module/python-selenium-chrome#section5-3

time.sleep(3)
html = driver.page_source


# html にソースが入ったので、これ以降はLXMLスクレイピングのコーディングとなる
root = lxml.html.fromstring(html)
path = root.xpath("//div[@class='txt']")
for p in path:  
    text =p.text_content()
    print(text)