from django.shortcuts import render
from django.views.generic import TemplateView

class BidderView(TemplateView):
    template_name = 'list.html'
