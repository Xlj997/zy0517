from django.contrib import admin
from .models import vote,option

# django自带强大的后台管理系统
# 在这里注册模型
# Register your models here.
admin.site.register(vote)
admin.site.register(option)