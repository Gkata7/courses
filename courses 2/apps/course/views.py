from django.shortcuts import render,redirect
from .models import Courses

def index(request):
    course = Courses.objects.all()
    context={
        'courses': course
    }
    return render(request, 'html/index.html',context)

def add(request):
    course = Courses.objects.create(course_name=request.POST['name'], description= request.POST['description'])
    return redirect('/')

def delete(request,id):
    remove= Courses.objects.get(id=id)
    remove.delete()
    return redirect('/')

def remove(request,id):
    context={
        'course': Courses.objects.get(id=id)
    }
    return render(request, 'html/delete.html', context)
