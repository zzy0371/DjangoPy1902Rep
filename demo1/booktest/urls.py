from django.conf.urls import url
from . import views

app_name = 'booktest'

urlpatterns = [
    url(r'^list/$',views.list, name="list"),
    url(r'^detail/(\d+)/$',views.detail,name="detail"),

    # url 参数 第一个代表正则表达式  第二个代表视图函数  第三个代表url名字
    url(r'^index/$',views.index,name="index"),
    """
    解除静态文件硬编码
    1/给应用添加命名空间
    2、给路由添加名字
    3、在模板中使用格式   {% url '命名空间名：路由名' 参数1 参数2 %}
    """
]