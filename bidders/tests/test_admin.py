# coding:utf8

import pytest
from mixer.backend.django import mixer
from django.contrib.admin.sites import AdminSite
from .. import admin, models


pytestmark = pytest.mark.django_db


class TestAdmin:
    def test_list(self):
        obj = mixer.blend('bidders.Bidder', # app.model
            name='주식회사 이노지투비',
            desc='업무용 소프트웨어 개발 전문')
        site = AdminSite()

        bidder_admin = admin.BidderAdmin(models.Bidder, site)
        result = bidder_admin.excerpt(obj)
        assert result == '주식회사 이노지투비'
