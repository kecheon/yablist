# coding: utf8

from django.test import RequestFactory
from django.test import TestCase
from django.core.urlresolvers import resolve
from django.views.generic import ListView
import pytest
from selenium import webdriver
import time
from cms.test_utils.testcases import CMSTestCase
from django.test.utils import override_settings
from .. import views
from categories.models import Category
from mixer.backend.django import mixer
from django.contrib.auth.models import AnonymousUser
from bidders.models import Bidder


pytestmark = pytest.mark.django_db

class SmokeTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)
        self.browser.get('http://localhost:8000')
        assert u'홈페이지' in self.browser.title


class TestViews(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.category = mixer.blend(Category, name=u'조달업체')

    def tearDown(self):
        self.browser.quit()

    def test_anonymous(self):
        req = RequestFactory().get('/categories/')
        categorytree_dict = {
            'queryset': Category.objects.filter(level=0)
        }

        user = AnonymousUser()
        req.user = user
        res = ListView.as_view(**categorytree_dict)(req)
        assert res.status_code == 200
        print(res.context_data)

    @override_settings(ROOT_URLCONF='categories.tests.urls')
    def test_url_resolves_to_categories_page(self):
        found = resolve('/categories/')
        assert found.view_name == 'categories_tree_list'

    def test_home_page_returns_correct_html(self):
        self.browser.get('http://localhost:8000/categories')
        assert u'조달업체' in self.browser.page_source

    def test_entry_listing_within_a_category(self):
        self.browser.get('http://localhost:8000/categories')
        self.browser.find_element_by_link_text(u'조달업체').click()
        time.sleep(1)
        assert u'견본 업체' in self.browser.page_source
