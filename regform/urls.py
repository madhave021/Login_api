from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^register/$', views.register, name='register'),
]