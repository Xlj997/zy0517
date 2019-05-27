from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse
from .models import Category,Article,Tag,ADS
from django.views.generic import View
# Paginator分页器   page分页
from django.core.paginator import Paginator
# 导入markdown
import markdown
# Create your views here.
from comments.forms import CommentForm


from PIL import Image,ImageDraw,ImageFont
import random,io

from django.core.mail import send_mail
from django.conf import settings

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


class Contacts(View):

    def get(self, request):
        cf = CommentForm()
        return render(request, 'contact.html', locals())

    def post(self,request):


        # 向HR发送邮件
        send_mail('测试邮件','这是一封测试邮件',settings.DEFAULT_FROM_EMAIL,['412239635@qq.com'])




        cf = CommentForm(request.POST)
        cf.save()
        cf = CommentForm()
        return render(request,'contact.html',{'info':'成功','cf':cf})


class Addads(View):


    def get(self,request):
        return render(request, 'addads.html')

    def post(self,request):
        img  = request.FILES['img']
        desc = request.POST.get('desc')
        ad = ADS(img=img,desc=desc)
        ad.save()

        return redirect(reverse('blog:index'))




def verify(request):



    # 每次请求验证码,需要使用 pillow构造出图像,返回

    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20,100),
    random.randrange(20,100),
    random.randrange(20,100))
    width = 100
    heigth = 25

    # 创建画面对象
    im = Image.new('RGB',(width,heigth),bgcolor)

    # 创建画笔对象
    draw = ImageDraw.Draw(im)

    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width),random.randrange(0, heigth))
        fill = (random.randrange(0, 255),255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'

    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象
    font = ImageFont.truetype('SCRIPTBL.TTF', 23)
    fontcolor = (255, random.randrange(0, 255),
    random.randrange(0, 255))

    # 绘制4个字
    draw.text((5, 2),
    rand_str[0], font=font,
    fill=fontcolor)
    draw.text((25, 2),
    rand_str[1],
    font=font,
    fill=fontcolor)
    draw.text((50, 2),
    rand_str[2],
    font=font,
    fill=fontcolor)
    draw.text((75, 2),
    rand_str[3],
    font=font,
    fill=fontcolor)

    # 释放画笔
    del draw
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f,'png')

    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')

