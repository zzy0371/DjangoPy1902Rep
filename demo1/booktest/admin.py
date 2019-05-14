from django.contrib import admin
from .models import BookInfo,HeroInfo
# Django自带强大的后台管理
# Register your models here.

admin.site.register(BookInfo)
admin.site.register(HeroInfo)
