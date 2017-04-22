# coding: utf-8

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class CategoriesAppHook(CMSApp):
    name = _('CategoriesApp')
    app_name = 'categories'
    def get_urls(self, page=None, language=None, **kwargs):
        return ['categories.urls']

apphook_pool.register(CategoriesAppHook)
