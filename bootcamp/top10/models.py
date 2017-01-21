from __future__ import unicode_literals
from django.db import models

class Top10(models.Model):
    print "top10 model"
#name="name"
# address="addr"
#date="1024"
    name = models.TextField(max_length=225)
    address = models.TextField(max_length=225)
    date = models.TextField(max_length=225)
