from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('',views.index,name='tasks'),
    path('new_task',views.add_tasks,name='new_task'),
    path('add_tag',views.add_tag,name = 'add_tags'),
    #path('',TemplateView.as_view(template_name='pages/home.html'),name ='home'),
    #path('about',TemplateView.as_view(template_name = 'pages/about.html'),name = 'about'),

    path('contact',views.contact,name = 'contact_us'),

]