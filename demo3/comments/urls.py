from django.conf.urls import url
from . import views
app_name = "comments"
urlpatterns = [
    url(r'^addcomment/(\d+)/$', views.AddComment.as_view(), name='addcomment' )
]
