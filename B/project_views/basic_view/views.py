from django.shortcuts import render
# Create your views here.

def index(request):
    return render (request, 'basic_view/home.html', {})

def blog(request):
    return render (request, 'basic_view/blog.html', {})

def mentee(request):
    return render (request, 'basic_view/mentee.html', {})

def mentor(request):
    return render (request, 'basic_view/mentor.html', {})

def author(request):
    return render (request, 'basic_view/author.html', {})