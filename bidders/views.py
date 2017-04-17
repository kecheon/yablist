from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView
from .models import Bidder
from categories.models import Category


class BidderList(ListView):
    model = Bidder


class CategoryListView(ListView):
    model = Category
    template_name = "categories/category_list.html"
    context_object_name = 'categories_all'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['bidders'] = Bidder.objects.all()
        return context
