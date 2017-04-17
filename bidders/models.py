# coding: utf8
from django.db import models


class Bidder(models.Model):
    name = models.CharField(max_length=100)
    number = models.BigIntegerField()
    desc = models.TextField()
    category = models.ForeignKey('categories.Category')
