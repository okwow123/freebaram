'''
how to find top 30 address from freebaram site?
'''

import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib
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
print max_no
print result[first_index:first_index+57]
#4.find 30 url address


