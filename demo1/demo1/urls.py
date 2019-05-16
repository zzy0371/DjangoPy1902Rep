"""demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    项目路由
"""
from django.contrib import admin
from django.urls import path
# 引入url函数
from django.conf.urls import url,include
from django.http import HttpResponse


# 项目路由  所有浏览器的请求先进入项目路由
urlpatterns = [
    #  http://127.0.0.1:8000/admin/

    path('admin/', admin.site.urls),
    # 引入外部路由配置文件
    # 会截取url中booktest字符串
    url('booktest/', include('booktest.urls', namespace='booktest'))

]
