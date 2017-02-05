import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib
# div id ="view_content" 

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open('http://broadcamp.com/bbs/login.php')
#br.open('http://broadcamp.com/bbs/board.php?bo_table=d4')
br.select_form(nr=0)
br.form['mb_id'] = 'okwow123'
br.form['mb_password'] = '239184'
br.submit()
#br.open('http://broadcamp.com/bbs/board.php?bo_table=d4&wr_id=3751')
br.open('http://broadcamp.com/bbs/board.php?bo_table=d4')
result=br.response().read()
first_index= result.find('http://broadcamp.com/bbs/board.php?bo_table=d4&wr_id=')
#no max value?
print result[first_index:first_index+57]
#session_requests = requests.session()
#br.open("http://broadcamp.com/bbs/board.php?bo_table=d4")
#print br.response().read()
#result=session_requests.get('http://broadcamp.com/bbs/board.php?bo_table=d4')
#print result.text
#print br.response().read()

