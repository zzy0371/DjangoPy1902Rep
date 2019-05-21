"""
使用Django form类自动生成表单元素

"""

from .models import MyUser

from django import forms


class LoginForm(forms.Form):
    """
    手动构造登录表单  确定 麻烦
    """
    username = forms.CharField(min_length=5,max_length=10,required=True,widget=forms.TextInput,error_messages={"min_length":"不能少于5个字符","max_length":"不能多于十个字符","required":"必填用户名"})

    password = forms.CharField(min_length=5,max_length=10,required=True,widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    """
    由模型类自动生成表单
    """
    class Meta():
        model = MyUser
        fields = ["url"]



