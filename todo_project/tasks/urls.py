from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='tasks'),
    path('new_task',views.add_tasks,name='new_task'),
    path('contact',views.contact,name = 'contact_us'),
    path('contact2',views.contact_2,name = 'contact_us_2'),
    path('new_task_2',views.add_tasks_2,name = 'add_task_2')
]