from django.db import models

# Create your models here.
# MVT  中的M
# ORM 中的O

# 一个表对应一个模型类
class BookInfo(models.Model):
    # 每一个字段对应 表中的一列
    title = models.CharField(max_length=30)
    # auto_now_add=True 意味着默认时间为 该行插入时间
    pub_date = models.DateTimeField(auto_now_add=True)

    # 打印模型
    def __str__(self):
        return self.title


class HeroInfo(models.Model):
    name = models.CharField(max_length=30)
    # bool 类型性别  默认值为true 代表男
    gender = models.BooleanField(default=True)
    # null = True 代表该列可以为空
    skill = models.CharField(max_length=50,null=True)
    # ForeignKey 表名和BookInfo为多对一关系
    # book 的类型 BookInfo
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

