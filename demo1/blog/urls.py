from django.conf.urls import url

from .models import Category,Tag,Article
from . import views


app_name='blog'


urlpatterns = [

    url(r'^index/$', views.index, name='index'),
    url(r'^single/(\d+)/$', views.single, name='single'),



]