from django.conf.urls import url
from django.contrib.auth import views as default_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^logout/$', default_views.logout, {'next_page': '/searcher/'}),
]
