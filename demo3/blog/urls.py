from django.conf.urls import url
from . import views
app_name = 'blog'
urlpatterns = [

    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^archives/(\d+)/(\d+)/$', views.archives, name='archives'),
    url(r'^category/(\d+)/$',views.category,name='category'),
    url(r'^tag/(\d+)/$', views.tag,name='tag'),
    url(r'^$', views.index, name='index'),
]
