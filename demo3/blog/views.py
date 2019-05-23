from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse
from .models import Article,Category,Tag
#  Paginator  Page
from django.core.paginator import Paginator
import markdown
from comments.forms import CommentForm
# Create your views here.

def index(request):
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum==None  else pagenum
    # 得到所有文章
    articles = Article.objects.all().order_by("-views")

    paginator = Paginator(articles,1)
    # 传入页码得到一个页面   page包含所有信息
    page = paginator.get_page(pagenum)
    page.parms = "/"
    return render(request,'index.html',{"page":page})

def detail(request, id):
    article = get_object_or_404(Article, pk = id )
    # 使用markdown处理body  将markdown语法转换为html标签
    article.views +=1
    # 确保body字段没有更改
    article.save()
    # 第一种使用  针对需要处理的article.body 将markdown转为html'
    # article.body = markdown.markdown(article.body, extensions = [
    #     "markdown.extensions.extra",
    #     "markdown.extensions.codehilite",
    #     "markdown.extensions.toc"
    # ])

    # 第二种如果在外部使用目录  需要使用构造函数的写法
    mk = markdown.Markdown(extensions=[
        "markdown.extensions.extra",
        "markdown.extensions.codehilite",
        "markdown.extensions.toc"
    ] )

    article.body = mk.convert(article.body)
    # 将markdown 中的目录赋予article的toc对象

    article.toc = mk.toc

    cf = CommentForm()
    return render(request,'single.html', locals())

def archives(request,year,month):
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum

    # 属性名__比较类型 =
    articles = Article.objects.filter(create_time__year =year , create_time__month = month )
    paginator = Paginator(articles, 1)
    # 传入页码得到一个页面   page包含所有信息
    page = paginator.get_page(pagenum)
    page.parms = "/archives/%s/%s/"%(year,month)
    return render(request, 'index.html', {"page": page})

def category(request,id):

    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum

    articles = get_object_or_404(Category,pk=id).article_set.all()
    paginator = Paginator(articles, 1)
    # 传入页码得到一个页面   page包含所有信息
    page = paginator.get_page(pagenum)
    page.parms = "/category/%s/"%(id,)
    return render(request, 'index.html', {"page": page })

def tag(request,id):
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum

    articles = get_object_or_404(Tag, pk=id).article_set.all()
    paginator = Paginator(articles, 1)
    # 传入页码得到一个页面   page包含所有信息
    page = paginator.get_page(pagenum)
    page.parms = "/tag/%s/"%(id,)
    return render(request, 'index.html', {"page": page})




