# -*- coding: utf8 -*-
import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib
import re
import sqlite3
from dateutil.parser import parse
conn=sqlite3.connect('/home/top10.db')
conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
item = [[u'']*3 for x in xrange(50)]
index=0
#1.go to site with login
cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open('http://broadcamp.com/bbs/login.php')
br.select_form(nr=0)
br.form['mb_id'] = 'okwow123'
br.form['mb_password'] = '239184'
br.submit()
br.open('http://broadcamp.com/bbs/board.php?bo_table=d4')
#2.save scratch results
result=br.response().read()
#3.find max no 
first_index= result.find('http://broadcamp.com/bbs/board.php?bo_table=d4&wr_id=')
max_no=result[first_index+53:first_index+57]
#print result[first_index:first_index+57]
#4.find 30 address,title,opendate
for x in range(50):
    taddress=result[first_index:first_index+53]+str(int(max_no)-x)
    br.open(taddress)
    tresult=br.response().read()
    title=tresult.split('<title>')[1].split('</title>')
    temp=title[0].replace('> 사이트 추천등록 | 브로드캠프','') 
    item[index][1]=temp
    ttresult=tresult.split('<div id=\"view_content\">')[1].split('<!--view_content-->[0]')
    match=re.search(r'(\d+월 +\d+일)',tresult)
    if match:
        mnd = match.group(1).replace('월','.').replace('일','')
        item[index][2]=mnd.replace(' ','')
    match=re.search(r'(\d+/+\d)',tresult)
    if match:
        mnd = match.group(1)
        item[index][2]=mnd.replace(' ','').replace('/','.')
    match=re.search(r'(\d+/ +\d)',tresult)
    if match:
        mnd = match.group(1)
        item[index][2]=mnd.replace(' ','').replace('/','.')
    match=re.search(r'(\d+ /+\d)',tresult)
    if match:
        mnd = match.group(1)
        item[index][2]=mnd.replace(' ','').replace('/','.')
    match=re.search(r'(\d+월+\d+일)',tresult)
    if match:
        mnd = match.group(1).replace('월','.').replace('일','')
        item[index][2]=mnd.replace(' ','')
    urls=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ttresult[0])
    item[index][2]='2017.'+item[index][2]
    if len(item[index][2])>8 or len(item[index][2])==5:
        item[index][2]=''
    else:
        date_obj=parse(item[index][2])
        item[index][2]=date_obj.strftime("%Y-%m-%d")
    print item[index][2]
    for y in range(len(urls)):
        if urls[y].find("broadcamp") == -1 and urls[y].find("google") == -1 and urls[y].find("schema") == -1 and  urls[y].find("miwit") == -1 and  urls[y].find("-") == -1 and  urls[y].find("<") == -1 and  urls[y].find("image") == -1 and urls[y] != '' and len(urls[y])>5:
            item[index][0]=urls[y]
            #br.open(urls[y])
            #tttresult=br.response().read()
            break
    conn.execute('insert into top10(address,name,date) values (?,?,?)',item[index])
    index+=1
conn.commit()
'''
for x in range(30):
    print item[x][0]+' '+item[x][1]+' '+item[x][2]
'''
#tresult=re.search('<div id=\"view_content\">[1].split<!--view_content-->[0]',tresult)
#print tresult.group()

