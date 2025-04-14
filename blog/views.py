from django.shortcuts import render, redirect, get_object_or_404

from blog.models import Blog


# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def ajouter_blog(request):
    return render(request, 'blog/ajouter_blog.html')

def liste_blog(request):
    liste_blogs = Blog.objects.all()
    context = {'liste_blogs': liste_blogs}
    return render(request, 'blog/liste_blog.html', context)

def modifier_blog(request, blog_id):
    return render(request, 'blog/modifier_blog.html', {'blog_id': blog_id})

def supprimer_blog(request, blog_id):
    return render(request, 'blog/supprimer_blog.html', {'blog_id': blog_id})

def blog_details(request, blog_id):
    return render(request, 'blog/blog_details.html', {'blog_id': blog_id})

def commenter_blog(request, blog_id):
    return render(request, 'blog/commenter_blog.html', {'blog_id': blog_id})