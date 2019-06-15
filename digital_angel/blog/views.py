from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # the keys of context are gonna be available in the template
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
