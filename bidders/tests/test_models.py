import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestBidder:
    def test_bidder_init(self):
        obj = mixer.blend('bidders.Bidder')
        assert obj is not None
