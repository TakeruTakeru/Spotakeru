from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name="index"),
    url(r'^chat/(?P<pk>[0-9]+)$', views.post_detail, name="host"),
    url(r'^chat/makedata/', views.post_make, name='post_make'),
    url(r'^check_spotify/$', views.check_spotify),
]
