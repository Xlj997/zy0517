"""poll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    项目路由
"""
from django.contrib import admin
from django.urls import path
# 引入路由绑定函数
from django.conf.urls import url,include

# 项目路由  所有浏览器的请求先进入项目路由

urlpatterns = [
    path('admin/', admin.site.urls),
    # 引入外部路由配置文件
    url('a/', include('poor.urls', namespace='poor'))
]


"""
解除静态文件硬编码

1.给应用添加命名空间
2.给路由添加名字
3.在模板中使用{% url 命名空间名：路由名 参数1 参数2 %}


"""
