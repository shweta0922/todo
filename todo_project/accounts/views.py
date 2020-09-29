from django.contrib.auth import authenticate , login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CreateUserForm
# Create your views here.




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('dashboard')

    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request,'accounts/register.html', {'form': form})

def logout(request):

    return  None