from django.db import models

# Create your models here.
# 用来写写模型
# mvt中的m
# orm中的o


# 一个表对应一个模型类
# 每一个字段对应表中的每一列
# 每个类必须继承于models.Model


# 创建问题模板类
class vote(models.Model):
    # 问题是字符串   最大长度为100
    problem = models.CharField(max_length=100,verbose_name='问题')


    #打印模型
    def __str__(self):
        return self.problem

# 创建选项模板类
class option(models.Model):
    # 字符串最大长度为30
    name = models.CharField(max_length=30,verbose_name='选项')
    # 所填内容为整数
    number = models.IntegerField(verbose_name='个数')
    # 设置外键  关联的是问题对象  关联类型是吉连
    vote = models.ForeignKey(vote,on_delete=models.CASCADE,verbose_name='问题')




    # 打印模型
    def __str__(self):
        return self.name

# 创建用户模板类
class user(models.Model):
    # 用户名 最大长度为30
    username = models.CharField(max_length=30, verbose_name='用户名')
    # 密码  最大长度为30
    pwd = models.CharField(max_length=30, verbose_name='密码')
    # 管理员表示  如果值是1表示是管理员 如果是0表示不是管理员
    root = models.CharField(max_length=30, verbose_name='管理员')

    # 打印模型
    def __str__(self):
        return self.username


