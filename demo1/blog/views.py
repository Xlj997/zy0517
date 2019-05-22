from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Article,Tag
# Create your views here.






def index(request):
    # return HttpResponse('123')
    return render(request,'index.html')

def single(request,id):
    return render(request, 'single.html')


