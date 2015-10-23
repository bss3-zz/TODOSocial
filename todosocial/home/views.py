from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render, render_to_response

from home.forms import *
from api.models import *


# Create your views here.
def index(request):
	if request.user is not None and request.user.is_authenticated():
		return HttpResponseRedirect(reverse('todo'))
	else:
		return render(request, 'index.html')

def todo(request):
	if request.user is not None and request.user.is_authenticated():
		context = {};
		user = request.user.first_name
		todos = Todo.objects.filter(owner = request.user)

		for t in todos:
			tasks = Task.objects.filter(owner = request.user, todo = t)
			for k in tasks:
				comments = Comment.objects.filter(owner = request.user, task = k)
				k.comments = comments
			t.tasks = tasks

		return render(request, 'todolist.html', {'name': user, 'todos': todos})
	else:
		return HttpResponseRedirect(reverse('index'))

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username = username, password = password)
			if user is not None:
				auth_login(request, user)
				return HttpResponseRedirect(reverse('todo'))
			else:
				return HttpResponseRedirect(reverse('index'))
		else:
			return HttpResponseRedirect(reverse('index'))
	else:
		return HttpResponseRedirect(reverse('index'))

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect(reverse('index'))
