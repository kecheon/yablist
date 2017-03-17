from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView
from .models import Bidder


class BidderList(ListView):
    model = Bidder
