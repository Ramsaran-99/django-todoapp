from django.shortcuts import render,redirect
from .models import List

# Create your views here.

def start(request):
    return render(request,'start.html')


def homepage(request):
    list=List.objects.all()
    if request.method=="POST":
        heading=request.POST.get('heading')
        description=request.POST.get('description')

        new_description=List(
            task=description,
            task_heading=heading,
        )
        new_description.save()

    return render(request,'trial/index2.html',
                  {
                      "lists":list,
                  })

def delete(request,id):
    if request.method=="POST":
        list=List.objects.get(id=id)
        list.delete()
    return redirect("home")

    