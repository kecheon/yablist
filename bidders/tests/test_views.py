from django.test import RequestFactory
from .. import views

class TestBidderListView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        res = views.BidderList.as_view()(req)
        assert res.status_code == 200
