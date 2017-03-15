from django.test import RequestFactory
from .. import views

class TestBidderView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        res = views.BidderView.as_view()(req)
        assert res.status_code == 200
