from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='patient'),url(r'^register/$', views.register, name='register')
]
