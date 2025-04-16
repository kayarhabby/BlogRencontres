from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import ContactForm
from blog.models import Blog, Comments
from django.templatetags.static import static
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
