from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views.generic import View
from django.http import HttpResponse
from .models import Comment
from blog.models import Article
from .forms import CommentForm
# Create your views here.

class AddComment(View):
    def post(self,request,id):

        article = get_object_or_404(Article,pk=id)



        cf = CommentForm(request.POST)

        if cf.is_valid():
            name = cf.cleaned_data['name']
            email = cf.cleaned_data['email']
            url = cf.cleaned_data['url']
            comment = cf.cleaned_data['comment']

        # name = request.POST.get('name')
        # emal = request.POST.get('emal')
        # url = request.POST.get('url')
        # comment = request.POST.get('comment')

            c = Comment()
            c.username = name
            c.email = email
            c.url = url
            c.content = comment
            c.article = article
            c.save()


            return redirect(reverse('blog:single',args=(id,)))
            # return HttpResponse('qqqq')

        else:
            return HttpResponse('评论不合法')

