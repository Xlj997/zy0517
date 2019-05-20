from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import vote, option, user
# Create your views here.
# mvt中的v  可以是视图函数  也可以是视图类

# 视图接口
# 请求（request）
# 响应（response）


def list(request):

    a = vote.objects.all()
    # print(a)

    return render(request, 'p/list.html', {'a': a})

def tp(request,id):

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


def tj(request):
    if request.method == 'POST':
        a = vote(problem=request.POST.get('wt'))
        a.save()
        for i in request.POST.getlist('xx'):
            option(name=i, number=0, vote=a).save()
        #     print(i)
        #
        #
        # print(request.POST.get('wt'))
        # print(request.POST.getlist('xx'))
        return render(request, 'p/list.html', )
    a = [1,2]
    return render(request, 'p/tj.html', {'a': a})



def logion(request):
    if request.method == 'POST':
        zh = request.POST.get('zh')
        pwd = request.POST.get('pwd')
        print(zh)
        user1 = user.objects.filter(username=zh)
        print(user1)
        aaa = request.POST.get('zhuce')
        print(aaa)
        if aaa == '注册':
            a1 = '注册失败'
            if len(user1) == 0:
                a1 = '注册成功'
                if zh[0] == ':':
                    user(username=zh[1:], pwd=pwd, root=1).save()
                    return redirect(reverse('poor:logion'), args=locals())
                user(username=zh, pwd=pwd, root=0).save()
                return redirect(reverse('poor:logion'), args=locals())
            print(locals())
            return redirect(reverse('poor:logion'))


        if pwd == user1[0].pwd:
             # request.session['name']=zh

            return redirect(reverse('poor:list'), args=locals())
        return redirect(reverse('poor:logion'))


    return render(request,'p/logion.html')