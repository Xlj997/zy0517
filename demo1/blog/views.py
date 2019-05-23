from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse
from .models import Category,Article,Tag

# Paginator分页器   page分页
from django.core.paginator import Paginator
# 导入markdown
import markdown
# Create your views here.
from comments.forms import CommentForm




# 首页视图函数
def index(request):
    # 根据GET请求的字段得到参数  这个参数是分页的页数
    pagenum = request.GET.get('page')
    # 判断有咩有传过来参数   如果没有传过来就等于一 如果传过来就等于传过来的参数
    pagenum = 1 if pagenum ==None else pagenum
    print(pagenum)

    # return HttpResponse('123')
    # 根据文章模板的管理器找到所有的文章  按照views排序   前面加负号是倒序
    arcticles = Article.objects.all().order_by('-views')
    # 调用分页得到分页器  参数第一个是要分页的对象  第二个是每一页所要的对象
    paginator = Paginator(arcticles,1)
    # 由分页器得到参数呢一页的所有内容   参数是传过来的参数是代表的是要第几页
    page = paginator.get_page(pagenum)

    # page.previous_page_number()
    # page.has_previous()
    #
    # page.has_next()
    # page.next_page_number()

    return render(request,'index.html',{'page':page})
# 内容页视图函数
def single(request,id):
    # 跟据ID找文章对象  用的方法是官方提供 封装好的不报错
    arcticle =get_object_or_404(Article,pk=id)
    arcticle.views += 1
    arcticle.save()
    # 使用markdown处理body(内容)  将markdown语法转化为html标签


    # markdown第一种用法  针对需要处理的内容  将markdown转化为html
    # arcticle.body = markdown.markdown(arcticle.body,extensions=[
    #     'markdown.extensions.extra',
    #     'markdown.extensions.codehilite',
    #     'markdown.extensions.toc',
    # ])


    # 第二种   如果在外部使用目录   需要使用构造函数的写法
    # markdown的渲染
    mk = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',

    ])
    arcticle.body = mk.convert(arcticle.body)
    # 把markdown生成的toc目录动态赋予给arcticle的toc对象
    arcticle.toc = mk.toc

    cf = CommentForm()

    return render(request, 'single.html',locals())




def archives(request,year,month):
    articles = Article.objects.filter(create_time__year=year, create_time__month=month)

    # 调用分页得到分页器  参数第一个是要分页的对象  第二个是每一页所要的对象
    paginator = Paginator(articles, 1)
    # 由分页器得到参数呢一页的所有内容   参数是传过来的参数是代表的是要第几页
    page = paginator.get_page(1)

    return render(request,'index.html',{'page': page})



def category(request,id):
    articles = get_object_or_404(Category,pk=id).article_set.all()

    # 调用分页得到分页器  参数第一个是要分页的对象  第二个是每一页所要的对象
    paginator = Paginator(articles, 1)
    # 由分页器得到参数呢一页的所有内容   参数是传过来的参数是代表的是要第几页
    page = paginator.get_page(1)

    return render(request, 'index.html', {'page': page})

def tag(request,id):
    articles = get_object_or_404(Tag, pk=id).article_set.all()


    # 调用分页得到分页器  参数第一个是要分页的对象  第二个是每一页所要的对象
    paginator = Paginator(articles, 1)
    # 由分页器得到参数呢一页的所有内容   参数是传过来的参数是代表的是要第几页
    page = paginator.get_page(1)

    return render(request, 'index.html', {'page': page})


def contactus(request):
    return render(request, 'contact.html')