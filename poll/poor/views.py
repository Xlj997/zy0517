from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import vote, option, user
# Create your views here.
# mvt中的v  可以是视图函数  也可以是视图类

# 视图接口
# 请求（request）
# 响应（response）







# list视图函数
def list(request):
    # 找到所有问题
    a = vote.objects.all()

    b = request.session.get('name')
    # print(b)

    # 返回列表页面并把问题对象当作参数返回出去
    return render(request, 'p/list.html', {'a': a,'b':b})


# 投票视图函数
def tp(request,id):
    # 判断如果请求方式是GET
    if request.method == 'GET':
        # 跟据对面传过来的参水找到这个问题的对象找到所有的问题
        a = vote.objects.get(pk=id).option_set.all()
        # print(type(a))
        # 返回到投票页面  并把参数返回出去
        return render(request, 'p/tp.html', {'a': a, 'b': id})
    # 判断  如果请求方式是POST
    elif request.method == 'POST':
        # 先找到POST表单提交过来的参数 找到对象
        b = option.objects.get(name=request.POST['ai'])
        # 让这个对象的某个字段加一
        b.number = int(b.number) + 1
        # 最后提交操作  实现投票加一的功能
        b.save()

        # print(request.POST['ai'])
        # 结束操作后返回重定向路由
        return HttpResponseRedirect('/a/xp/%s'%(id,))


# 投票显示视图函数
def xp(request,id):
    # 通过传过来的参数找到对象
    b = vote.objects.get(pk=id)
    # 通过对象  用一找多的方法找到这个对象下的所有选项
    a = b.option_set.all()

    # 返回显示页面  包含参数
    return render(request, 'p/xp.html', {'a': a, 'b': b})

# 添加问题函数
def tj(request):
    # 判断如果请求方式是POST
    if request.method == 'POST':
        # 先获取表单传过来的参数  然后构建对象那个
        a = vote(problem=request.POST.get('wt'))
        # 最后提交对象
        a.save()
        # 获取表单传过来的参数,这个参数是列表  需要遍历 每一个都添加到选项表 外键是上面所创建的问题表
        for i in request.POST.getlist('xx'):
            option(name=i, number=0, vote=a).save()
        # 添加问题成功后返回列表页面
        return render(request, 'p/list.html', )
    a = [1,2]
    # 如果请求方式不是POST 那就返回添加页面
    return render(request, 'p/tj.html', {'a': a})



def logion(request):
    if request.method == 'POST':

        # 根据表单传过来的数据找到提交的用户名字和密码
        zh = request.POST.get('username')
        pwd = request.POST.get('password')
        # print(zh)
        # 通过表单传过来的用户名字在用户表里面找对应的对象
        user1 = user.objects.filter(username=zh)
        aaa = request.POST.get('zhuce')
        # print(zh)
        # print(pwd)
        print(aaa)
        if aaa == '登陆':
            if len(user1)==0:
                a ='用户不存在'
                return render(request,'p/logion.html', {'a': a})
            else:
                if user1[0].pwd == pwd:
                    request.session['name'] = zh
                    return redirect(reverse('poor:list'))
        if aaa == '注册':
            print('111111')
            # 如果在用户表里面找到的对象列表长度是0  代表这个用户名可用  可以注册
            if len(user1) == 0:
                # 那么变量等于注册成功
                a = '注册成功'
    #             # 判断表单提交过来的用户名的第一个是否是 : 如果是那么他有管理员权限
                print(zh)
                if zh[0] == ':':
                    user(username=zh[1:], pwd=pwd, root=1).save()
                  # 返回到登陆页面
                    return render(request,'p/logion.html', {'a': a})
    #             # 如果不是管理员  那么注册普通股用户
                user(username=zh, pwd=pwd, root=0).save()
    #             # 返回登陆页面
                return render(request,'p/logion.html', {'a': a})
            else:
                a = '已有用户请重试'
                return render(request, 'p/logion.html', {'a': a})
    if request.method == 'GET':
        return render(request, 'p/logion.html')


    #
    # # 判断请求是否是POST
    # if request.method == 'POST':
    #     # 根据表单传过来的数据找到提交的用户名字和密码
    #     zh = request.POST.get('username')
    #     pwd = request.POST.get('password')
    #     # print(zh)
    #     # 通过表单传过来的用户名字在用户表里面找对应的对象
    #     user1 = user.objects.filter(username=zh)
    #     # print(user1)
    #     # 根据表单传过来的数据找到提交的按钮是呢个
    #     aaa = request.POST.get('zhuce')
    #     print(zh)
    #     print(pwd)
    #     print(aaa)
    #     如果提交按钮是注册
    #     if aaa == '注册':
    #         # 定义一个空变量
    #         a1 = None
    #         # 如果在用户表里面找到的对象列表长度是0  代表这个用户名可用  可以注册
    #         if len(user1) == 0:
    #             # 那么变量等于注册成功
    #             a1 = '注册成功'
    #             # 判断表单提交过来的用户名的第一个是否是 : 如果是那么他有管理员权限
    #             if zh[0] == ':':
    #                 user(username=zh[1:], pwd=pwd, root=1).save()
    #                 # 返回到登陆页面
    #                 return redirect(reverse('poor:logion'), args=locals())
    #             # 如果不是管理员  那么注册普通股用户
    #             user(username=zh, pwd=pwd, root=0).save()
    #             # 返回登陆页面
    #             return redirect(reverse('poor:logion'), args=locals())
    #         # print(locals())
    #         如果找到服务器里面用户对象列表长度不是零代表这个用户名已存在不能再次注册 返回登陆页面注册
    #     return redirect(reverse('poor:logion'))
    #
    #     如果表单提交的不是注册  那么执行登陆功能  用登陆的密码 和登陆的用户名所在服务器里面找到的密码匹配
    #     如果相等那么登陆成功
    #     if pwd == user1[0].pwd:
    #         # 把数据存在session里面
    #         request.session['name']=zh
    #         # 返回列表页
    #         return redirect(reverse('poor:list'), args=locals())
    #     # 如果登陆密码错误 登陆失败  返回登陆页面
    #     return redirect(reverse('poor:logion'))
    #
    # # 如果请求不是POST  那么返回登陆页面
    # return render(request,'p/logion.html')





def zc(request):
    if request.method=='POST':
        pass
