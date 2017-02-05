'''
how to find top 30 address from freebaram site?
'''

import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib
import re
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
#4.find 30 url address
print "30 url?"
for x in range(1):
    taddress=result[first_index:first_index+53]+str(int(max_no)-x)
    br.open(taddress)
    tresult=br.response().read()
    print tresult.split('<div id=\"view_content\">')[1].split('<!--view_content-->[0]')
#tresult=re.search('<div id=\"view_content\">[1].split<!--view_content-->[0]',tresult)
#print tresult.group()

