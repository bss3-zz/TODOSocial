#django
from django.conf.urls import include, url

#django-rest

#api
from home.views import *

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'todo/', todo, name='todo'),
	url(r'login/', login, name='login'),
	url(r'logout/', logout, name='logout'),
]