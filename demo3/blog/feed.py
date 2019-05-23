"""
RSS  可以通过RSS聚合工具来完成网站订阅
如何支持订阅：需要将内容包装成符合RSS规范的XML格式
通过重写Feed类完成XML格式内容包装
"""
from django.contrib.syndication.views import Feed
from .models import Article
from django.shortcuts import reverse
class BlogFeed(Feed):
    title = "zzy的个人博客"
    description = "一个很好地学习网站"
    link = "/"

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body[:30]

    def item_link(self, item):
        return reverse('blog:detail', args=(item.id,))