from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.CategoryListView.as_view()),
    # url(r'^/categories', views.Categories.as_view()),
]
