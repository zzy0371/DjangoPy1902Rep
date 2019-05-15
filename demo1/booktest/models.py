from django.db import models

# Create your models here.
# MVT  中的M
# ORM 中的O

# 一个表对应一个模型类
class BookInfo(models.Model):
    # 每一个字段对应 表中的一列
    title = models.CharField(max_length=30, verbose_name="书名")
    # auto_now_add=True 意味着默认时间为 该行插入时间
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="出版时间")

    # 打印模型
    def __str__(self):
        return self.title


# 用于选择性别的选项
GENDER = ( ("man","男"),("woman","女"))

class HeroInfo(models.Model):
    name = models.CharField(max_length=30, verbose_name="角色名")
    # bool 类型性别  默认值为true 代表男
    # gender = models.BooleanField(default=True, verbose_name="性别")

    # 拥有choice之后gender 成了下拉列表
    gender = models.CharField(max_length=10,choices=GENDER)

    # 在后台重写显示字段
    def genderinfo(self):
        return self.gender
    genderinfo.short_description = "角色性别"


    # null = True 代表该列可以为空 针对数据库
    # black = True 针对表单可以为空
    skill = models.CharField(max_length=50,blank=True, null=True,verbose_name= "绝招")
    # ForeignKey 表名和BookInfo为多对一关系
    # book 的类型 BookInfo
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE, verbose_name="书")

    def __str__(self):
        return self.name

