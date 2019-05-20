from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import vote,option
# Create your views here.
# mvt中的v  可以是视图函数  也可以是视图类

# 视图接口
# 请求（request）
# 响应（response）


def list(request):

    a = vote.objects.all()

    return render(request, 'p/list.html', {'a':a})

def tp(request,id):
    # print(id)
    # print(request.method)
    # for i in dir(request):
    #
    #     print(i)

    if request.method == 'GET':

        a = vote.objects.get(pk=id).option_set.all()
        print(type(a))
        return render(request, 'p/tp.html', {'a': a, 'b': id})

    elif request.method == 'POST':

        b = option.objects.get(name=request.POST['ai'])
        b.number = int(b.number) + 1
        b.save()

        print(request.POST['ai'])




        return HttpResponseRedirect('/a/xp/%s'%(id,))



def xp(request,id):
    b = vote.objects.get(pk=id)
    a = b.option_set.all()


    return render(request, 'p/xp.html', {'a': a, 'b': b})