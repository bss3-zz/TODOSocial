from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def todo(request):
    return render(request, 'todolist.html')