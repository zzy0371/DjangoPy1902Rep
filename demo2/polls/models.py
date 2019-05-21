from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=50,verbose_name="问题描述")
    class Meta():
        verbose_name = "问题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ChoiceManage(models.Manager):
    def incresevotes(self, id):
       c = self.get(pk =id)
       c.votes += 1
       c.save()

class Choice(models.Model):
    title = models.CharField(max_length=50, verbose_name="选项描述")
    votes = models.IntegerField(default=0, verbose_name="得票数")
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    objects = ChoiceManage()
    class Meta():
        verbose_name = "选项"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class MyUser(User):
    url = models.URLField(blank=True, null=True, default="http://www.baidu.com")
    class Meta():
        verbose_name = "用户"
        verbose_name_plural = verbose_name
