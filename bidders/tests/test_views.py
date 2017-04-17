from django.test import RequestFactory
from .. import views
import pytest
pytestmark = pytest.mark.django_db

class TestBidderListView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        res = views.BidderList.as_view()(req)
        assert res.status_code == 200
        print(res.context_data)
