# -*- coding: utf8 -*-
import re
result='free baram open 2017 year 2월 17 go server'
#rresult=result.split(' ')
#print rresult
match=re.search(r'(\d+월 +\d+일)',result)
if match:
    print match.groups()
