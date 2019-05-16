from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BookInfo,HeroInfo
# Create your views here.
# MVT 中的V  可以是视图函数 也可以是视图类

# 视图 接口

def index(request):
    # print(10/0)
    # return  HttpResponse("index首页")
    # 1 加载模板
    template = loader.get_template("booktest/index.html")
    # 2 构造参数字典
    contex = {"username":"zzy" }
    # 3 使用模板渲染动态数据
    result = template.render(contex)
    return HttpResponse(result)

def list(request):
    # 查询所有的书籍
    allbook = BookInfo.objects.all()

    templ = loader.get_template('booktest/list.html')
    result = templ.render({"allbook": allbook  })
    return HttpResponse(result)

def detail(request,id):
    print(id)
    # id 代表书的主键
    book = None
    try:
        book = BookInfo.objects.get(pk = id )
    except Exception as e:
        return HttpResponse("没有书籍信息")

    templ = loader.get_template('booktest/detail.html')
    result = templ.render({"book": book})
    return HttpResponse(result)