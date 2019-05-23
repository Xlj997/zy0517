from django.conf.urls import url

from .models import Category,Tag,Article
from . import views
from . import feed


app_name = 'blog'


urlpatterns = [

    url(r'^index/$', views.index, name='index'),
    url(r'^single/(\d+)/$', views.single, name='single'),
    url(r'^archives/(\d+)/(\d+)/$', views.archives, name='archives'),
    url(r'^category/(\d+)/$', views.category, name='category'),
    url(r'^tag/(\d+)/$', views.tag, name='tag'),

    url(r'^rss/$',feed.BlogFeed(),name='rss'),
    url(r'^contactus/$', views.contactus, name='contactus')
]