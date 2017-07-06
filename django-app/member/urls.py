from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views


app_name = 'member'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'member/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'member:login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]