from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import ContactForm
from blog.models import Blog, Comments, Team, Gallery
from django.templatetags.static import static
# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def liste_blog(request):
    liste_blogs = Blog.objects.all()
    context = {
        'title': 'Blog',
        'current_page': 'Blog',
        'banner_image': static('blog/images/gallery/lookMeInTheEyes.jpg'),
        'liste_blogs': liste_blogs
    }
    return render(request, 'blog/blog.html', context)

def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'title': 'Blog Details',
        'current_page': 'Blog Details',
        'banner_image': static('blog/images/gallery/reveals.jpg'),
        'blog': blog
    }
    return render(request, 'blog/blog_details.html', context)

def commenter_blog(request, blog_id):
    # obtenir l'ensemble des commentaires pour le blog
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comments.objects.filter(blog=blog)
    context = {'blog': blog, 'comments': comments}
    return render(request, 'blog/commenter_blog.html', context)

def contact(request):
    context = {
        'title': 'Contact',
        'current_page': 'Contact',
        'banner_image': static('blog/images/my-heart-is-yours.jpg'),
        'form': ContactForm(request.POST or None)  # Ajout du formulaire ici
    }
    # Traitement du formulaire après soumission
    if request.method == 'POST' and context['form'].is_valid():
        context['form'].save()
        return redirect('blog:contact')  # Redirige après soumission réussie

    return render(request, 'blog/contact.html', context)

def about(request) :
    context = {
        'title': 'About',
        'current_page': 'About',
        'banner_image': static('blog/images/my-heart-is-yours.jpg'),
        'about_image_1' : static('blog/images/my-heart-is-yours.jpg'),
        'about_image_2' : static('blog/images/life_is_better.jpg'),
        'about_image_3' : static('blog/images/you_make_my_heart_skip_a_bit.jpg'),
    }
    return render(request, 'blog/about.html', context)

def team(request):
    teams = Team.objects.all()
    context = {
        'title': 'Team',
        'current_page': 'Team',
        'banner_image': static('blog/images/my-heart-is-yours.jpg'),
        'list_teams': teams,
    }
    return render(request, 'blog/team.html', context)

def gallery(request):
    galleries = Gallery.objects.all()
    context = {
        'title': 'Gallery',
        'current_page': 'Gallery',
        'banner_image': static('blog/images/my-heart-is-yours.jpg'),
        'list_gallery': galleries,
    }
    return render(request, 'blog/gallery.html', context)

def service(request):
    context = {
        'title': 'Service',
        'current_page': 'Service',
        'banner_image': static('blog/images/my-heart-is-yours.jpg'),
        'service_image' : static('blog/images/made-it-come-true.jpg'),
    }
    return render(request, 'blog/service.html', context)

def error(request):
    return render(request, 'blog/error.html')