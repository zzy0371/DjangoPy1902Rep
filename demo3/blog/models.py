from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "分类"
        verbose_name_plural = verbose_name

class Tag(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "标签"
        verbose_name_plural = verbose_name

class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    auther = models.ForeignKey(User,models.CASCADE)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "文章"
        verbose_name_plural = verbose_name


