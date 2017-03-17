# coding: utf8
import pytest
from ..cms_apps import BiddersAppHook
pytestmark = pytest.mark.django_db


class TestCmsApp:

    def test_init(self):
        hook = BiddersAppHook()
        assert hook.app_name == "조달업체"
        assert hook.name == "조달업체 앱"

        assert hook.get_urls() == ["bidders.urls"]
