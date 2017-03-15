# coding: utf8

import pytest
from mixer.backend.django import mixer
from .. import models
pytestmark = pytest.mark.django_db


class TestBidder:
    def test_bidder_init(self):
        obj = mixer.blend('bidders.Bidder')
        assert obj.pk == 1

    def test_get_bidder(self):
        obj = mixer.blend(
            'bidders.Bidder',
            name="주식회사 이노지투비",
            number=1298676066,
            desc='업무용 웹S/W 개발 전문'
        )
        bidder = models.Bidder.objects.first()
        assert bidder.name == '주식회사 이노지투비'
