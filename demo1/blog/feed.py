'''

rss  可以通过RSS聚合工具来完成网站支持订阅
如何支持订阅  需要将内容包装成符合RSS规范的xml合适
通过重写Feed类完成XML格式内容的包装

'''


from django.contrib.syndication.views import Feed
from .models import Article
from django.shortcuts import reverse

class BlogFeed(Feed):
    title = '95的个人博客'
    description = '呵呵哈哈嘎嘎嘿嘿'
    link = '/blog/index/'

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.body[:30]
    def item_link(self, item):
        return reverse('blog:single',args=(item.id,))






