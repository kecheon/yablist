# coding: utf8

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class BiddersAppHook(CMSApp):
    app_name = "조달업체"
    name = "조달업체 앱"

    def get_urls(self, page=None, language=None, **kwargs):
        return ['bidders.urls']

apphook_pool.register(BiddersAppHook)
