#django
from django.contrib.auth.models import User

#django-rest
from rest_framework import serializers

#api
from api.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email',)

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('id', 'text',)

class CommentSerializerCreate(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('id', 'task', 'owner', 'text',)

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('id', 'description', 'completed', 'deadline', 'position',)

class TaskSerializerCreate(serializers.ModelSerializer):
	comments = CommentSerializer(source='comment_set', many = True, read_only = True)
	class Meta:
		model = Task
		fields = ('id', 'todo', 'owner', 'description', 'completed', 'deadline', 'position', 'comments',)

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = ('id','title',)

class TodoSerializerCreate(serializers.ModelSerializer):
	tasks = TaskSerializer(source='task_set', many = True, read_only = True)
	class Meta:
		model = Todo
		fields = ('id', 'owner', 'title', 'tasks',)