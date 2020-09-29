

from django.shortcuts import render, redirect

# Create your views here.
from .forms import ContactForm, TaskForm, TagForm
from .models import Tasks, Tag


def index(request):
    tasks = Tasks.objects.all()
    tags = Tag.objects.all()
    return render(request,'tasks/index.html',{'tasks':tasks,'tags' : tags})



def add_tasks(request):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    return  render(request,'tasks/new_task.html',{'form':form})

def add_tag(request):
    if request.method == 'POST':
        form = TagForm(data=request.POST)
        if form.is_valid():
            new_tag=form.save()
            return redirect('tasks')
    else:
        form = TagForm()
    return render(request,'tasks/add_tag.html',{'form': form})


def contact(request):
    if request.method == 'POST':
       form = ContactForm(data=request.POST)
       if form.is_valid():
           return redirect('tasks')
    else:
        form = ContactForm()
    return  render(request,'tasks/contact_us.html',{'form':form})




