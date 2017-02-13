# -*- coding: utf8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest,\
                        HttpResponseForbidden

from bootcamp.top10.models import Top10
import sqlite3

def DisplayTop10(request):
    conn = sqlite3.connect('/home/top10.db')
    cur = conn.cursor()
    cur.execute('select name,address,date from top10 where name not like "%홍보%" group by date order by date desc')
    top10s=cur.fetchall()
    conn.close()
#print type(top10s[0])
#   return HttpResponse(top10s[0][0])
    return render(request, 'feeds/top10.html',{
        'top1name': top10s[0][0],
        'top1addr': top10s[0][1],
        'top1date': top10s[0][2],

        'top2name': top10s[1][0],
        'top2addr': top10s[1][1],
        'top2date': top10s[1][2],

        'top3name': top10s[2][0],
        'top3addr': top10s[2][1],
        'top3date': top10s[2][2],

        'top4name': top10s[3][0],
        'top4addr': top10s[3][1],
        'top4date': top10s[3][2],

        'top5name': top10s[4][0],
        'top5addr': top10s[4][1],
        'top5date': top10s[4][2],

        'top6name': top10s[5][0],
        'top6addr': top10s[5][1],
        'top6date': top10s[5][2],

        'top7name': top10s[6][0],
        'top7addr': top10s[6][1],
        'top7date': top10s[6][2],

        'top8name': top10s[7][0],
        'top8addr': top10s[7][1],
        'top8date': top10s[7][2],

        'top9name': top10s[8][0],
        'top9addr': top10s[8][1],
        'top9date': top10s[8][2],

        'top10name': top10s[9][0],
        'top10addr': top10s[9][1],
        'top10date': top10s[9][2],

        })

#return HttpResponse(top10s)
#return render(request, 'top10.html')
#result=Top10.objects
#print Top10.objects
#top10Info="name: {0}; address: {1}; date: {2}".format(result.name,result.address,result.date)
#return render(request, 'top10/top10.html',{ 'welcome_text': top10Info })
