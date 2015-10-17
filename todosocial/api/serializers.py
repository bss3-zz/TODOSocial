#django
from django.contrib.auth.models import User

#django-rest
from rest_framework import serializers

#api
from api.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		field = ('username', 'email',)

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('id', 'owner', 'text',)

class TaskSerializer(serializers.ModelSerializer):
	comments = CommentSerializer(source='comment_set', many = True, read_only = True)
	class Meta:
		model = Task
		fields = ('id', 'owner', 'description', 'completed', 'deadline', 'position', 'comments',)

class TodoSerializer(serializers.ModelSerializer):
	tasks = TaskSerializer(source='task_set', many = True, read_only = True)
	class Meta:
		model = Todo
		fields = ('id', 'owner', 'title', 'tasks',)