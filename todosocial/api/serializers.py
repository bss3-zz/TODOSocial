#django
from django.contrib.auth.models import User

#django-rest
from rest_framework import serializers

#api
from api.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = ('id', 'title', 'user')

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('id', 'description', 'completed', 'deadline', 'position')

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = ('id', 'text')