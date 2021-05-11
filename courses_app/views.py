from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request, "index.html", context)

def add_course(request):
    if request.method == "POST":
        errors = Course.objects.validator(request.POST)

        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/')
        
        new_course = Course.objects.create(name=request.POST['name'])
        desc = Description.objects.create(description=request.POST['description'], course = new_course)

    return redirect('/')

def show_course(request, id):
    context = {
        'this_course' : Course.objects.get(id=id)
    }

    return render(request, "course.html", context)

def add_comment(request, id):
    if request.method=="POST":
        this_course = Course.objects.get(id=id)

        this_comment = Comment.objects.create(comment=request.POST['comment'], course = this_course)

        print(f"Course: {this_course.name}"
        )
        print(f"Comment: {this_comment.comment}")
        print(f"Course Comments: {this_course.comments.all()}")

    return redirect(f"/{id}")

def destroy(request, id):
    context = {
        "this_course" : Course.objects.get(id=id)
    }
    return render(request, 'delete.html', context)

def confirm_destroy(request, id):
    destroy = Course.objects.get(id=id)
    destroy.delete()
    return redirect('/')