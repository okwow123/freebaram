# -*- coding: utf8 -*-
import requests
import sqlite3

# connction sqlite3
conn = sqlite3.connect('/home/top10.db')
c = conn.cursor()
from bs4 import BeautifulSoup
# 2-array 
item = [[u'']*3 for x in xrange(20)]
#start scratch
url='http://top.cafe.daum.net/_c21_/search?search_opt=name&sort_type=recent&q=%ED%94%84%EB%B0%94&search_type=tab'+str(1)
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'lxml')
index = 0
for link in soup.select('div > div > a'):
    #print link
    href=link.get('href')
    if href[0:20]=='http://cafe.daum.net':
        name = soup.find_all("a", class_="link_tit #cafename#result#name")
        date = soup.find_all("div", class_="info_scafe")
        index2=date[index].get_text().index(': 201')+1
        
        # save the data
        address=href
        name=name[index].get_text()
        date=date[index].get_text()[index2:len(date[index].get_text())].strip()
        item[index][0]=address
        item[index][1]=name
        item[index][2]=date
        c.execute('insert into top10(address,name,date) values (?,?,?)',item[index])
        index+=1
conn.commit()
