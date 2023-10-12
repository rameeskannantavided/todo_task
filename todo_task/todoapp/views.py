from django.shortcuts import render, redirect
from .models import Todo
from .form import TodoForm
# Create your views here.
def add(request):
    task1 = Todo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Todo(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'tasks':task1})

def delete(request,id):
    task = Todo.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task = Todo.objects.get(id=id)
    f = TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')

    return render(request,'update.html',{'f':f,'tasks':task})
