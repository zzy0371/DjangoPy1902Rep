from django.shortcuts import redirect,reverse
# 调用流程
# 将index函数作为fun实参传入checklogin 并且执行执行check()
def checklogin(fun):
    def check(request,*args):
        # 在cookie去用户
        # un = request.COOKIES.get('username')
        print(request.user,'++++++')
        print(request.user.is_authenticated)
        # 在session中取
        # un = request.session.get("username")
        # if un:
        #     return fun(request,*args)
        # else:
        #     return redirect(reverse('polls:login'))


        if request.user and request.user.is_authenticated:
            return fun(request, *args)
        else:
            return redirect(reverse('polls:login'))

    return check