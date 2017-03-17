from django.contrib import admin
from . import models


class BidderAdmin(admin.ModelAdmin):
    model = models.Bidder
    list_display = ('excerpt', )

    def excerpt(self, obj):
        return obj.name

admin.site.register(models.Bidder, BidderAdmin)
