from django.contrib import admin
from .models import vote,option

# django自带强大的后台管理系统
# 在这里注册模型
# Register your models here.
# 注册问题模型
admin.site.register(vote)
# 注册选项模型
admin.site.register(option)