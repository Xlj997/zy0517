from django.conf.urls import url
from . import views

app_name = 'poor'
urlpatterns = [

    # url参数  第一个代表正则表达式  第二个代表视图函数   第三个代表url名字
    # 投票页面路由
    url(r'^tp/(\d+)/$', views.tp,name='tp'),
    # 列表页面路由
    url(r'^list/$', views.list, name='list'),
    # 投票显示路由
    url(r'^xp/(\d+)/$', views.xp, name='xp'),
    # 添加问题路由
    url(r'^tj//$', views.tj, name='tj'),
    # 登陆页面路由
    url(r'^logion/$', views.logion, name='logion'),
    #注册路由
    url(r'^zc/$', views.zc, name='zc'),

    url(r'^checkuser/$', views.checkuser, name='checkuser'),



]