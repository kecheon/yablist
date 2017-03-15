# coding:utf8

import pytest
from mixer.backend.django import mixer
from django.contrib.admin.sites import AdminSite
from .. import admin, models


pytestmark = pytest.mark.django_db


class TestAdmin:
    def test_list(self):
        obj = mixer.blend('bidders.Bidder', name='주식회사 이노지투비')
        site = AdminSite()

        bidder_admin = admin.BidderAdmin(models.Bidder, site)
        result = bidder_admin.excerpt(obj)
        assert result == '주식회사 이노지투비'
