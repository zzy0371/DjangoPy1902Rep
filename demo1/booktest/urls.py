from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$',views.list),
    url(r'^detail/(\d+)/$',views.detail),
    url(r'^index/$',views.index),
]