from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice,MyUser
from .util import checklogin
from django.views.generic import View
from django.contrib.auth import authenticate,login as lgi,logout as lgo


# class Login(View):
#     def get(self,request):
#         return render(request,'polls/login.html')
#     def post(self,request):
#         username = request.POST.get("username")
#         if username == "zzy":
#             # 登录成功之后需要将用户相关cookie存储
#             res = redirect(reverse('polls:index'))
#             res.set_cookie("username",username)
#             return res
#         else:
#             return render(request, 'polls/login.html',{"error":"用户名错误"})

def login(request):
    if request.method == "GET":
        return render(request, 'polls/login.html',{"py1902":'<h1>HelloWorld</h1>'})
    else:
        # 没有使用Django自带用户系统
        # username = request.POST.get("username")
        # if username == "zzy":
        #     # 登录成功之后需要将用户相关cookie存储
        #     res = redirect(reverse('polls:index'))
        #     # 设置cookit完成登录
        #     # res.set_cookie("username", username)
        #     # 通过session完成登录
        #     request.session["username"] = username
        #     return res
        # else:
        #     return render(request, 'polls/login.html', {"error": "用户名错误"})

        username = request.POST.get("username")
        pwd = request.POST.get("password")
        # MyUser.objects.filter(username = username, p)
        user = authenticate(request, username = username,password = pwd)
        if user:
            print(user)
            lgi(request,user)
            return redirect(reverse('polls:index'))
        else:
            return render(request, 'polls/login.html', {"error": "用户名或者密码错误"})


def logout(request):
    res = redirect(reverse('polls:login'))
    # res.delete_cookie("username")
    # 清除session登录信息
    # request.session.flush()

    #  调用退出登录方法
    lgo(request)
    return res


def regist(request):
    if request.method == "POST":
        username = request.POST.get("username_regi")
        pwd = request.POST.get("password_regi")
        pwd2 = request.POST.get("password_regi_2")
        error = None
        if pwd != pwd2:
            error = "密码不一致"
            return render(request, 'polls/login.html', {"error": error})
        else:
            MyUser.objects.create_user(username= username, password=pwd, url = 'http://zzy0371.com')
            return redirect(reverse('polls:login'))



# class Index(View):
#     def get(self,request):
#         questions = Question.objects.all()
#         return render(request, 'polls/index.html', locals())

@checklogin
def index(request):
    username = request.session.get('username')
    questions = Question.objects.all()
    return render(request,'polls/index.html', locals())



# class Detail(View):
#     def get(self,request,id):
#         question = Question.objects.get(pk=id)
#         return render(request, 'polls/detail.html', locals())
#
#     def post(self,request,id):
#         c_id = request.POST["choice"]
#         Choice.objects.incresevotes(c_id)
#
#         return HttpResponseRedirect('/polls/result/%s/' % (id,))

@checklogin
def detail(request,id):
    question = Question.objects.get(pk = id)
    if request.method == "POST":
        c_id = request.POST["choice"]
        Choice.objects.incresevotes(c_id)

        return HttpResponseRedirect('/polls/result/%s/'%(id,))

    return render(request,'polls/detail.html', locals())

# class Result(View):
#     def get(self,request,id):
#         question = Question.objects.get(pk=id)
#         return render(request, 'polls/result.html', locals())

@checklogin
def result(request,id):
    question = Question.objects.get(pk=id)
    return render(request, 'polls/result.html', locals())