from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
	title = models.CharField(max_length = 50)
	user = models.OneToOneField(User)

class Task(models.Model):
	todo = models.ForeignKey(Todo)
	description = models.CharField(max_length = 150)
	completed = models.BooleanField(default = False)
	deadline = models.DateField(blank = False)
	position = models.IntegerField()

class Comment(models.Model):
	task = models.ForeignKey(Task)
	text = models.TextField(max_length = 1000)
