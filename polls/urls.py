from sys import path

from django.conf.urls import url
from . import views

app_name = 'mypack'
urlpatterns = [
    url(r'^sign/$', views.signup, name='sign'),
    url(r'^login/$',views.login,name='login'),

    url(r'^emp/$', views.employee, name='emp'),

    url(r'^user/$',views.enduser,name='user'),




]
