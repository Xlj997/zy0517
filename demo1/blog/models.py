from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.




# 种类
class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='种类')

    def __str__(self):
        return self.title


# 标签表类
class Tag(models.Model):
    title = models.CharField(max_length=30,verbose_name='标签类')

    def __str__(self):
        return self.title


# 文章表类
class Article(models.Model):
    # 标题
    title = models.CharField(max_length=30,verbose_name='文章标题')
    # 文本区域
    body = models.TextField(verbose_name='文章内容')
    # 连接种类
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='种类')
    # 发布时间
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    # 更改时间
    update_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')
    # 作者
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
    # 连接标签  多对多
    tags = models.ManyToManyField(Tag,verbose_name='标签')
    # 阅读数  默认为0
    views = models.PositiveIntegerField(default=0,verbose_name='阅读数')



class MessageInfo(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True)
    subject = models.CharField(max_length=50)
    info = HTMLField()





