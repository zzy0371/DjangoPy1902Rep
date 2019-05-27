from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse
from .models import Article,Category,Tag,Ads as AdsModel
#  Paginator  Page
from django.core.paginator import Paginator
import markdown
from comments.forms import CommentForm
from django.views.generic import View
from .forms import ContactForm
from django.core.mail import send_mail,send_mass_mail
from django.conf import settings
from django.views.decorators.cache import cache_page
# Create your views here.

# @cache_page(timeout=60*2)
def index(request):
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum==None  else pagenum
    # 得到所有文章
    articles = Article.objects.all().order_by("-views")

    paginator = Paginator(articles,2)
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

class Contacts(View):
    def get(self,request):
        cf = ContactForm()
        return render(request, 'contact.html',locals())
    def post(self,request):
        # 向HR发送邮件
        try:
            send_mail("测试邮件", "请点击  <a href='http://127.0.0.1:8000/'>首页</a>", settings.DEFAULT_FROM_EMAIL, ["zhangzhaoyu@qikux.com", "496575233@qq.com"])
            # send_mass_mail((("测试邮件1", "邮件1", settings.DEFAULT_FROM_EMAIL, ["zhangzhaoyu@qikux.com", "496575233@qq.com"]),
            #                ("测试邮件2", "邮件2", settings.DEFAULT_FROM_EMAIL, [ "496575233@qq.com"]),
            #                ("测试邮件3", "邮件3", settings.DEFAULT_FROM_EMAIL, ["zhangzhaoyu@qikux.com"])))
        except Exception as e:
            print(e)

        cf = ContactForm(request.POST)
        cf.save()
        cf = ContactForm()
        return render(request, 'contact.html', {"info":'成功',"cf":cf})


class Ads(View):
    def get(self,request):
        return render(request,"addads.html")

    def post(self,request):
        img = request.FILES["img"]
        desc = request.POST.get("desc")
        ad = AdsModel(img = img, desc= desc)
        ad.save()
        return redirect(reverse('blog:index'))







