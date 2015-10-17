from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
	owner = models.ForeignKey(User)
	title = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.title

class Task(models.Model):
	owner = models.ForeignKey(User)
	todo = models.ForeignKey(Todo)
	description = models.CharField(max_length = 150)
	completed = models.BooleanField(default = False)
	deadline = models.DateField(null = True, blank = True)
	position = models.IntegerField()

	def __unicode__(self):
		return self.description + ' ' + str(self.completed) + ' ' + str(self.deadline)

class Comment(models.Model):
	owner = models.ForeignKey(User)
	task = models.ForeignKey(Task)
	text = models.TextField(max_length = 1000)

