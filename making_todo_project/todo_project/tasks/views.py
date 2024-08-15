from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def task_list(request):
    tasks=Task.objects.all()
    return render(request,'tasks/task_list.html',{'tasks':tasks})
def add_task(request):
    if request.method=='POST':
        task_name=request.POST.get('name')
        if task_name:
            Task.objects.create(name=task_name)
            return redirect('task_list')
    return render(request,'tasks/add_task.html')
def delete_task(request,task_id):
    task=Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

    