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
    # 标题
    title = models.CharField(max_length=30)
    # 文本区域
    body = models.TextField()
    # 连接种类
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    # 发布时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更改时间
    update_time = models.DateTimeField(auto_now=True)
    # 作者
    author = models.CharField(max_length=30)
    # 连接标签  多对多
    tags = models.ManyToManyField(Tag)

    views = models.PositiveIntegerField(default=0)



