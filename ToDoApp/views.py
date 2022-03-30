from django.shortcuts import redirect, render
from .models import ToDoList
# Creating views for todolist
def todolist(request):
    if request.method=='GET':
        todolists=ToDoList.objects.all()
        return render(request,'todolist.html',{'todolists':todolists})
    else:
        ToDoList(
            todolist=request.POST.get('task'),
            date=request.POST.get('datetime')
        ).save()
        todolists=ToDoList.objects.all()
        return render(request,'todolist.html',{'todolists':todolists})

# Creating views for Update TodoList
def updatetodolist(request,id):
    task=ToDoList.objects.get(id=id)
    return render (request,'todoupdate.html',{'task':task})

# Creating Views For Save Updated Data
def save_todotask(request,id):
    task=ToDoList.objects.get(id=id)
    task.todolist=request.POST.get('task')
    task.date=request.POST.get('datetime')
    task.save()
    return redirect('todolist')

# Creating Views  for Delete todolist

def delete_task(request,id):
    task=ToDoList.objects.get(id=id)
    task.delete()
    return redirect('todolist')
