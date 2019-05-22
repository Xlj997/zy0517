from django.db import models
from django.contrib.auth.models import User
# Create your models here.




# 种类
class Category(models.Model):
    title = models.CharField(max_length=30)


# 标签表类
class Tag(models.Model):
    title = models.CharField(max_length=30)


# 文章表类
class Article(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date1 = models.DateTimeField(auto_now_add=True)
    date2 = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=30)



