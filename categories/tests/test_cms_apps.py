# coding: utf-8

import pytest
from cms.apphook_pool import apphook_pool


def test_cms_apps_4_categories_app_hook():
    assert apphook_pool.get_apphook('CategoriesAppHook') is not None
