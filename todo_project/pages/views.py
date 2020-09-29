from django.shortcuts import render, redirect

# Create your views here.
from pages.forms import ContactForm


def contact(request):
    if request.method == 'POST':
       form = ContactForm(data=request.POST)
       if form.is_valid():
           return redirect('tasks')
    else:
        form = ContactForm()
    return  render(request,'pages/contact.html',{'form':form})