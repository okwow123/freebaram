# -*- coding: utf8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest,\
                        HttpResponseForbidden

from bootcamp.top10.models import Top10
import sqlite3

def DisplayTop10(request):
    conn = sqlite3.connect('/home/top10.db')
    cur = conn.cursor()
    cur.execute('select name,address,date from top10 group by date order by date desc')
    top10s=cur.fetchall()
    conn.close()
    return render(request, 'feeds/top10.html',{
        'top10s': top10s,
        })
#return HttpResponse(top10s)
#return render(request, 'top10.html')
#result=Top10.objects
#print Top10.objects
#top10Info="name: {0}; address: {1}; date: {2}".format(result.name,result.address,result.date)
#return render(request, 'top10/top10.html',{ 'welcome_text': top10Info })
