from django.shortcuts import render,redirect
from .models import TaskDb
from .forms import TaskForm
from django.contrib import messages

def home(request):
    if request.method == 'POST' :
        form = TaskForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = TaskDb.objects.all()
            messages.success(request,("New Item Added .."))
            return render(request,'index.html',{'all_items' : all_items})
        else :
            all_items = TaskDb.objects.all()
            return render(request,'index.html',{'all_items' : all_items})

    else :
        all_items = TaskDb.objects.all()
        return render(request,'index.html',{'all_items' : all_items})

def delete(request,list_id) :
    item = TaskDb.objects.get(pk = list_id)
    item.delete()
    messages.success(request,("Item deleted") )
    return redirect('home')
