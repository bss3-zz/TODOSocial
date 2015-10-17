#django
from django.conf.urls import include, url

#django-rest

#api
from api.views import *

urlpatterns = [
	url(r'^todo/$', TodoList.as_view(), name='todo_list'),
	url(r'^todo/(?P<pk>[0-9]+)$', TodoDetail.as_view(), name='todo_detail'),
	url(r'^task/$', TaskList.as_view(), name='task_list'),
	url(r'^task/(?P<pk>[0-9]+)$', TaskDetail.as_view(), name='task_detail'),
	url(r'^comment/$', CommentList.as_view(), name='comment_list'),
	url(r'^comment/(?P<pk>[0-9]+)$', CommentDetail.as_view(), name='comment_detail'),
]