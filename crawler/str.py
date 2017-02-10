result='free baram open 2017 year 02/17 go server'
rresult=result.split(' ')
print rresult
for x in range(len(rresult)):
    if rresult[x].find("server") != -1:
        print rresult[x]
