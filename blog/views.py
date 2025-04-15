from django.shortcuts import render, redirect, get_object_or_404

from blog.models import Blog, Comments

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def liste_blog(request):
    liste_blogs = Blog.objects.all()
    context = {'liste_blogs': liste_blogs}
    return render(request, 'blog/liste_blog.html', context)

def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {'blog': blog}
    return render(request, 'blog/blog_details.html', context)

def commenter_blog(request, blog_id):
    # obtenir l'ensemble des commentaires pour le blog
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comments.objects.filter(blog=blog)
    context = {'blog': blog, 'comments': comments}
    return render(request, 'blog/commenter_blog.html', context)