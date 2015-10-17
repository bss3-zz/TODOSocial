#django
from django.shortcuts import render

#django-rest
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

#api
from api.serializers import *
from api.models import *


#####TODO#####
class TodoList(ListCreateAPIView):
	serializer_class = TodoSerializerCreate

	#Listing all the todolists of a request user
	def get_queryset(self):
		user = self.request.user
		if user.is_superuser:
			return Todo.objects.all()
		else:
			return Todo.objects.filter(owner = user)

	def create(self, request, *args, **kwargs):
		user = self.request.user
		if user.is_superuser:
			return super(TodoList, self).create(request, *args, **kwargs)
		else:
			#Making the request user be the owner of the created todo list so user
			#does not have to pass the ownership field when creating
			request.data._mutable = True
			request.data['owner'] = user.id
			request.data._mutable = False
			return super(TodoList, self).create(request, *args, **kwargs)


class TodoDetail(RetrieveUpdateDestroyAPIView):
	serializer_class = TodoSerializer

	#get a todolist of a request user
	def get_queryset(self):
		user = self.request.user
		if user.is_superuser:
			return Todo.objects.filter(id = self.kwargs['pk'])
		else:
			return Todo.objects.filter(owner = user, id = self.kwargs['pk'])

	#Check the ownership for a single todo list
	def check_single_ownership(self, request, pk):
		user = request.user
		if user.is_superuser:
			return True
		else:	
			todo = Todo.objects.filter(owner = user, id = pk)
			return len(todo) == 1

	def update(self, request, *args, **kwargs):

		#Checking if the requester has the rights the current object
		if self.check_single_ownership(request, kwargs['pk']):
			return super(TodoDetail, self).update(request, *args, **kwargs)
		else:
			result = {'detail' : 'Not found.'}
			return Response(result,status=status.HTTP_404_NOT_FOUND)


	def delete(self, request, *args, **kwargs):
		#Checking if the requester has the rights the current object
		if self.check_single_ownership(request, kwargs['pk']):
			return super(TodoDetail, self).delete(request, *args, **kwargs)
		else:
			result = {'detail' : 'Not found.'}
			return Response(result,status=status.HTTP_404_NOT_FOUND)
#####TODO#####

#####TASK#####
class TaskList(ListCreateAPIView):
	serializer_class = TaskSerializerCreate

	#Listing all the tasks of a request user
	def get_queryset(self):
		user = self.request.user
		if user.is_superuser:
			return Task.objects.all()
		else:
			return Task.objects.filter(owner = user)

	def create(self, request, *args, **kwargs):
		user = self.request.user
		if user.is_superuser:
			return super(TaskList, self).create(request, *args, **kwargs)
		else:
			#Making the request user be the owner of the created task so user
			#does not have to pass the ownership field when creating
			request.data._mutable = True
			request.data['owner'] = user.id
			request.data._mutable = False

			return super(TaskList, self).create(request, *args, **kwargs)

class TaskDetail(RetrieveUpdateDestroyAPIView):
	serializer_class = TaskSerializer

	#Get one task of a request user
	def get_queryset(self):
		user = self.request.user
		if user.is_superuser:
			return Task.objects.filter(id = self.kwargs['pk'])
		else:
			return Task.objects.filter(owner = user, id = self.kwargs['pk'])

	#Check the ownership for a single task
	def check_single_ownership(self, request, pk):
		user = request.user
		if user.is_superuser:
			return True
		else:	
			task = Task.objects.filter(owner = user, id = pk)
			return len(task) == 1

	def update(self, request, *args, **kwargs):

		#Checking if the requester has the rights the current object
		if self.check_single_ownership(request, kwargs['pk']):
			return super(TaskDetail, self).update(request, *args, **kwargs)
		else:
			result = {'detail' : 'Not found.'}
			return Response(result,status=status.HTTP_404_NOT_FOUND)


	def delete(self, request, *args, **kwargs):
		#Checking if the requester has the rights the current object
		if self.check_single_ownership(request, kwargs['pk']):
			return super(TaskDetail, self).delete(request, *args, **kwargs)
		else:
			result = {'detail' : 'Not found.'}
			return Response(result,status=status.HTTP_404_NOT_FOUND)
#####TASK#####

#####COMMENT#####
class CommentList(ListCreateAPIView):
	serializer_class = CommentSerializerCreate

	#Listing all the comments of a request user
	def get_queryset(self):
		user = self.request.user
		if user.is_superuser:
			return Comment.objects.all()
		else:
			return Comment.objects.filter(owner = user)

	def create(self, request, *args, **kwargs):
		user = self.request.user
		if user.is_superuser:
			return super(CommentList, self).create(request, *args, **kwargs)
		else:
			#Making the request user be the owner of the created task so user
			#does not have to pass the ownership field when creating
			request.data._mutable = True
			request.data['owner'] = user.id
			request.data._mutable = False
			return super(CommentList, self).create(request, *args, **kwargs)

class CommentDetail(RetrieveUpdateDestroyAPIView):
	serializer_class = CommentSerializer

	#Get one comment of a request user
	def get_queryset(self):
		user = self.request.user
		if user.is_superuser:
			return Comment.objects.filter(id = self.kwargs['pk'])
		else:
			return Comment.objects.filter(owner = user, id = self.kwargs['pk'])

	#Check the ownership for a single comment
	def check_single_ownership(self, request, pk):
		user = request.user
		if user.is_superuser:
			return True
		else:	
			comment = Comment.objects.filter(owner = user, id = pk)
			return len(comment) == 1

	def update(self, request, *args, **kwargs):

		#Checking if the requester has the rights the current object
		if self.check_single_ownership(request, kwargs['pk']):
			return super(CommentDetail, self).update(request, *args, **kwargs)
		else:
			result = {'detail' : 'Not found.'}
			return Response(result,status=status.HTTP_404_NOT_FOUND)


	def delete(self, request, *args, **kwargs):
		#Checking if the requester has the rights the current object
		if self.check_single_ownership(request, kwargs['pk']):
			return super(CommentDetail, self).delete(request, *args, **kwargs)
		else:
			result = {'detail' : 'Not found.'}
			return Response(result,status=status.HTTP_404_NOT_FOUND)
#####COMMENT#####
