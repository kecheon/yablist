# coding: utf8
from django.db import models
from filer.fields.image import FilerImageField


class Bidder(models.Model):
    name = models.CharField(max_length=100)
    number = models.BigIntegerField()
    photo = FilerImageField(
        blank=True,
        help_text=u'사진 추가',
        null=True,
        on_delete=models.SET_NULL,
    )
    desc = models.TextField()
    address = models.CharField(max_length=200, null=True)
    category = models.ForeignKey('categories.Category')
    tags = models.ForeignKey('simpletext.SimpleCategory', null=True)
