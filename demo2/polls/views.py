from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice,MyUser
from .util import checklogin
from django.views.generic import View
from django.contrib.auth import authenticate,login as lgi,logout as lgo
from .forms import LoginForm,RegisterForm
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
# 引入序列化加密并且有效期信息
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,SignatureExpired
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
        # lf = LoginForm()
        # rf = RegisterForm()
        # return render(request, 'polls/login.html',{"lf":lf, "rf":rf})
        return render(request, 'polls/login.html')
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

        # 使用django授权系统
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        # MyUser.objects.filter(username = username, p)
        # user = authenticate(request, username = username,password = pwd)
        user = get_object_or_404(MyUser, username = username)
        if not user.is_active:
            return render(request, 'polls/login.html', {"error": "用户尚未激活"})
        else:
            check =  user.check_password(pwd)
            if check:
                lgi(request, user)
                return redirect(reverse('polls:index'))
            else:
                return render(request, 'polls/login.html', {"error": "用户名或者密码错误"})


        # print(user)
        # if user:
        #     print(user)
        #     if user.is_active:
        #         lgi(request,user)
        #         return redirect(reverse('polls:index'))
        #     else:
        #         return render(request, 'polls/login.html', {"error": "用户尚未激活"})
        # else:
        #     return render(request, 'polls/login.html', {"error": "用户名或者密码错误"})


        # 使用自动生成表单post
        # lf = LoginForm(request.POST)
        # if lf.is_valid():
        #     username = lf.cleaned_data["username"]
        #     pwd = lf.cleaned_data["password"]
        #     # MyUser.objects.filter(username = username, p)
        #     user = authenticate(request, username = username,password = pwd)
        #     if user:
        #         print(user)
        #         lgi(request,user)
        #         return redirect(reverse('polls:index'))
        #     else:
        #         return render(request, 'polls/login.html', {"error": "用户名或者密码错误"})




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
        email = request.POST.get("email")
        error = None
        if pwd != pwd2:
            error = "密码不一致"
            return render(request, 'polls/login.html', {"error": error})
        else:
            user = MyUser.objects.create_user(username= username, password=pwd, url = 'http://zzy0371.com')
            print(user.id,user.username,user.is_active)
            # 注册用户之后默认为非激活状态
            user.is_active = False
            user.save()

            # http://127.0.0.1:8000/7/
            # send_mail("点击激活用户", url, settings.DEFAULT_FROM_EMAIL,[email])

            # 为了防止非人为激活，需要将激活地址加密
            # 带有有效期的序列化
            # 1 得到序列化工具
            serutil = Serializer(settings.SECRET_KEY)
            # 2 使用工具对字典对象序列化
            result =  serutil.dumps({"userid": user.id }).decode("utf-8")
            # print(result, type(result))

            mail = EmailMultiAlternatives("点击激活用户","<a href = 'http://127.0.0.1:8000/polls/active/%s/'>点击激活</a>"%(result,),settings.DEFAULT_FROM_EMAIL,[email])
            mail.content_subtype = "html"
            mail.send()

            return render(request, 'polls/login.html', {"error": "请在一个小时之内激活"})


def active(request,info):
    serutil = Serializer(settings.SECRET_KEY)
    try:
        obj = serutil.loads(info)
        print(obj["userid"])
        id = obj["userid"]
        user = get_object_or_404(MyUser, pk=id)
        user.is_active = True
        user.save()
        return redirect(reverse('polls:login'))
    except SignatureExpired as e:
        return HttpResponse("过期了")




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