from django.shortcuts import render,redirect
from .models import List


def start(request):
    return render(request,'start.html')


def homepage(request):
    list=List.objects.all()
    if request.method=="POST":
        heading=request.POST.get('heading')
        description=request.POST.get('description')
        status=request.POST.get('sts')
        urgency=request.POST.get('urg')

        new_description=List(
            task=description,
            task_heading=heading,
            urgency=urgency,
            status=status,
        )
        new_description.save()

    return render(request,'index2.html',
                  {
                      "lists":list,
                  })

def delete(request,id):
    if request.method=="POST":
        list=List.objects.get(id=id)
        list.delete()
    return redirect("home")

    
'''

edit button
priority list
status
https://www.figma.com/community/file/1358477027647527963/to-do-list-web-app-design
reminder - sending mail before an hour



'''