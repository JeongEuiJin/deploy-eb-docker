from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^post/$', views.test, name='post')
]
