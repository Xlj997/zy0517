from django.conf.urls import url
from . import views

app_name = 'poor'
urlpatterns = [

    # url参数  第一个代表正则表达式  第二个代表视图函数   第三个代表url名字
    url(r'^tp/(\d+)/$', views.tp,name='tp'),
    url(r'^list/$', views.list, name='list'),
    url(r'^xp/(\d+)/$', views.xp, name='xp'),
    url(r'^tj//$', views.tj, name='tj'),

]