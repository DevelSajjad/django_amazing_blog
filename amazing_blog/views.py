from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'amazing_blog/frontend/index.html')

def about(request):
    return render(request, 'amazing_blog/frontend/about.html')

def contact(request):
    return render(request, 'amazing_blog/frontend/contact.html')

def category(request):
    return render(request, 'amazing_blog/frontend/category.html')

def postDetail(request):
    return render(request, 'amazing_blog/frontend/post-details.html')

def privacy(request):
    return render(request, 'amazing_blog/frontend/privacy.html')