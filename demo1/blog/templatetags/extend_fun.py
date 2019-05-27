# 导入这个类   这个类为了注册标签或者过滤器
from django import template
from ..models import Article,Category,Tag,ADS
register =template.Library()

# 定义过滤器

# 过滤器参数最多有两个

# 把参数转化为小写
@register.filter(name='mylower') #注册这个过滤器    name参数可以不写
def mylower(value):
    return value.lower()


# 截取前几个  第一个参数是对象  第二个参数是要截取的个数
@register.filter(name='myslice')  #注册这个过滤器
def myslice(value,lenth):
    return value[:lenth]





# 定义标签

# 标签可以有任意参数


@register.simple_tag
def getcategorys():
    return Category.objects.all()


# 获取最新文章
@register.simple_tag
def getlatestarticles(num=3):
    return Article.objects.all().order_by('-create_time')[:num]


# 获得所有发表过文章的月份
@register.simple_tag
def getarchives(num=3):
    return Article.objects.dates('create_time', 'month', order='DESC')[:num]

@register.simple_tag
def gettags():
    return Tag.objects.all()


@register.simple_tag
def getads():
    print(ADS.objects.all()[0].img)
    return ADS.objects.all()







