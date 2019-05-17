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


class Account(models.Model):
    username = models.CharField(max_length=20)



class Contact(models.Model):
    tel = models.CharField(max_length=11)
    acc = models.OneToOneField(Account,on_delete=models.CASCADE)


class Host(models.Model):
    hostname = models.CharField(max_length=20)

class Application(models.Model):
    appname = models.CharField(max_length=20)
    hosts = models.ManyToManyField(Host)

class ManageExt(models.Manager):
    def createtestmodel2(self, _title):
        t = self.model()
        t.title = _title
        t.save()

    def deletetestmodel2(self,_pk):
        self.get(pk = _pk).delete()



class TestModel(models.Model):
    title = models.CharField(max_length=20)
    # 添加字段  字段为模型管理器
    manage = models.Manager()
    # 应为manage2 继承了manage并且扩展了功能
    manage2 =  ManageExt()   #models.Manager()
    # 在模型类中封装方法，减少重复代码的编写
    @classmethod
    def createtestmodel(cls,_title):
        t = cls(title = _title)
        t.title = _title
        t.save()


    class Meta():
        db_table = 'testmodel1'
        ordering = ['-title']
        verbose_name = "测试模型类"
        verbose_name_plural = "测试模型类"



"""
一对多 A，B   比如关系定义在 B方
A找B  a.b_set.all()
B找A  b.关系字段

一对一 A，B   比如关系定义在B方
A找B  a.b
B找A  b.关系字段


多找多  A，B  比如关系定义在B方
插入关系
    b.关系字段名.add(a1,a2)
删除关系
    b.关系字段.remove(a1,a2)
清除所有关系
    b.关系字段.clear()
    
A找B  a.b_set.all()
B找A  b.关系字段.all()


"""
