from django.contrib import admin
from .models import BookInfo,HeroInfo,TestModel
# Django自带强大的后台管理
# Register your models here.

class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 1

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["title","pub_date"]
    list_filter = ["title", "pub_date"]
    search_fields = ["title", "pub_date"]
    list_per_page = 1
    inlines = [ HeroInfoInline]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["name", "gender", "genderinfo"]





admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)

admin.site.register(TestModel)
