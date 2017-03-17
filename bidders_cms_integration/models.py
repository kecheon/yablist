# coding: utf-8

from django.db import models
from cms.models import CMSPlugin
from bidders.models import Bidder

class BidderPluginModel(CMSPlugin):
    bidder = models.ForeignKey(Bidder, related_name="bidder")

    def __unicode__(self):
        return self.bidder.name
