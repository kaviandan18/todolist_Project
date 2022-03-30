
from django.contrib import admin
from django.urls import path
from ToDoApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.todolist , name='todolist'),
    path('todoupdate/<id>',views.updatetodolist,name='todoupdate'),
    path('save_update_todotask/<id>',views.save_todotask,name='savetodotask'),
    path('delete_todolist/<id>',views.delete_task,name='delete_todotask')

]
