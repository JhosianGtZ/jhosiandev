from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from datetime import date
import datetime


class Project(models.Model):

    title = CharField(max_length=35)

    subtitle = CharField(max_length=35, default="WEBSITE" , blank=True)

    date = models.DateField(datetime.date.today)

    imageurl = URLField()

    description = models.TextField()

    url = URLField(blank=True)

    icon1 = CharField(max_length=25)
    icon2 = CharField(max_length=25)
    icon3 = CharField(max_length=25)

