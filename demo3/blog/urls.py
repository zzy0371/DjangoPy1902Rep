from django.conf.urls import url
from . import views
app_name = 'blog'
urlpatterns = [

    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
]
