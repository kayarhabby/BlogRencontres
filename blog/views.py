from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from blog.forms import ContactForm
from blog.models import Blog, Comments, Team, Gallery, Contact
from django.templatetags.static import static
# import paginator
from django.core.paginator import Paginator
# Create your views here.

#def index(request):
#    return render(request, 'blog/index.html')

class IndexView(TemplateView):
    template_name = 'blog/index.html'
#def liste_blog(request):
#    blogs = Blog.objects.all()
    # Pagination
#    paginator = Paginator(blogs, 4)  # 4 blogs par page
#    page = request.GET.get('page')
#    liste_blogs  = paginator.get_page(page) # Récupérer la page demandée
#    context = {
#        'title': 'Blog',
#        'current_page': 'Blog',
#        'banner_image': static('blog/images/gallery/lookMeInTheEyes.jpg'),
#        'liste_blogs': liste_blogs,
 #       'blogs': blogs,
#    }
#    return render(request, 'blog/blog.html', context)

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'liste_blogs'
    paginate_by = 4  # Nombre de blogs par page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        context['current_page'] = 'Blog'
        context['banner_image'] = static('blog/images/gallery/lookMeInTheEyes.jpg')
        return context
    def get_queryset(self):
        queryset = super().get_queryset()
        # Vous pouvez ajouter des filtres ici si nécessaire
        # Exemple : queryset = queryset.filter(author='John Doe')
        # Vous pouvez également trier les résultats
        # Exemple : queryset = queryset.order_by('-created_at')
        # Vous pouvez également ajouter des annotations ou des agrégations
        # Exemple : queryset = queryset.annotate(num_comments=Count('comments'))
        # Vous pouvez également ajouter des préfetch_related ou select_related pour optimiser les requêtes
        # Exemple : queryset = queryset.prefetch_related('comments')
        # Exemple : queryset = queryset.select_related('author')
        return queryset

#def blog_details(request, blog_id):
#    blog = get_object_or_404(Blog, pk=blog_id)
#    context = {
#        'title': 'Blog Details',
#        'current_page': 'Blog Details',
#        'banner_image': static('blog/images/gallery/reveals.jpg'),
#        'blog': blog
#    }
#    return render(request, 'blog/blog_details.html', context)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_details.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog Details'
        context['current_page'] = 'Blog Details'
        context['banner_image'] = static('blog/images/gallery/reveals.jpg')
        return context
    def get_object(self, queryset=None):
        # Récupérer l'objet Blog en fonction de l'ID passé dans l'URL
        blog_id = self.kwargs.get('pk')
        return get_object_or_404(Blog, pk=blog_id)


#def contact(request):
#    context = {
#        'title': 'Contact',
#        'current_page': 'Contact',
#        'banner_image': static('blog/images/my-heart-is-yours.jpg'),
#        'form': ContactForm(request.POST or None)  # Ajout du formulaire ici
#    }
    # Traitement du formulaire après soumission
#    if request.method == 'POST' and context['form'].is_valid():
#        context['form'].save()
#        return redirect('blog:contact')  # Redirige après soumission réussie

#    return render(request, 'blog/contact.html', context)

class ContactFormView(CreateView):
    model= Contact
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = '/blog/contact/'  # URL de redirection après soumission réussie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        context['current_page'] = 'Contact'
        context['banner_image'] = static('blog/images/my-heart-is-yours.jpg')
        return context

    def form_valid(self, form):
        # Traitez le formulaire ici si nécessaire
        # Par exemple, vous pouvez envoyer un e-mail ou effectuer d'autres actions
        # Enregistrez le formulaire
        form.save()
        # Vous pouvez également rediriger vers une autre vue ou une URL spécifique
        #return redirect(self.success_url)
        # Si vous souhaitez rediriger vers la même page après la soumission réussie
        return super().form_valid(form)

#def about(request) :
#    context = {
#        'title': 'About',
#        'current_page': 'About',
#        'banner_image': static('blog/images/my-heart-is-yours.jpg'),
#       'about_image_1' : static('blog/images/my-heart-is-yours.jpg'),
#        'about_image_2' : static('blog/images/life_is_better.jpg'),
#        'about_image_3' : static('blog/images/you_make_my_heart_skip_a_bit.jpg'),
#    }
#    return render(request, 'blog/about.html', context)

class AboutView(TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About'
        context['current_page'] = 'About'
        context['banner_image'] = static('blog/images/my-heart-is-yours.jpg')
        context['about_image_1'] = static('blog/images/my-heart-is-yours.jpg')
        context['about_image_2'] = static('blog/images/life_is_better.jpg')
        context['about_image_3'] = static('blog/images/you_make_my_heart_skip_a_bit.jpg')
        return context



#def team(request):
#    teams = Team.objects.all()
#    context = {
#        'title': 'Team',
#        'current_page': 'Team',
#        'banner_image': static('blog/images/my-heart-is-yours.jpg'),
#        'list_teams': teams,
#    }
#    return render(request, 'blog/team.html', context)

class TeamListView(ListView):
    model = Team
    template_name = 'blog/team.html'
    context_object_name = 'list_teams'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Team'
        context['current_page'] = 'Team'
        context['banner_image'] = static('blog/images/my-heart-is-yours.jpg')
        return context
    def get_queryset(self):
        queryset = super().get_queryset()
        # Vous pouvez ajouter des filtres ici si nécessaire
        # Exemple : queryset = queryset.filter(author='John Doe')
        # Vous pouvez également trier les résultats
        # Exemple : queryset = queryset.order_by('-created_at')
        # Vous pouvez également ajouter des annotations ou des agrégations
        # Exemple : queryset = queryset.annotate(num_comments=Count('comments'))
        # Vous pouvez également ajouter des préfetch_related ou select_related pour optimiser les requêtes
        # Exemple : queryset = queryset.prefetch_related('comments')
        # Exemple : queryset = queryset.select_related('author')
        return queryset


#def gallery(request):
#    galleries = Gallery.objects.all()
#    context = {
#        'title': 'Gallery',
#        'current_page': 'Gallery',
#        'banner_image': static('blog/images/my-heart-is-yours.jpg'),
#        'list_gallery': galleries,
#    }
#    return render(request, 'blog/gallery.html', context)


class GalleryListView(ListView):
    model = Gallery
    template_name = 'blog/gallery.html'
    context_object_name = 'list_gallery'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gallery'
        context['current_page'] = 'Gallery'
        context['banner_image'] = static('blog/images/my-heart-is-yours.jpg')
        return context
    def get_queryset(self):
        queryset = super().get_queryset()
        # Vous pouvez ajouter des filtres ici si nécessaire
        # Exemple : queryset = queryset.filter(author='John Doe')
        # Vous pouvez également trier les résultats
        # Exemple : queryset = queryset.order_by('-created_at')
        # Vous pouvez également ajouter des annotations ou des agrégations
        # Exemple : queryset = queryset.annotate(num_comments=Count('comments'))
        # Vous pouvez également ajouter des préfetch_related ou select_related pour optimiser les requêtes
        # Exemple : queryset = queryset.prefetch_related('comments')
        # Exemple : queryset = queryset.select_related('author')
        return queryset

#def service(request):
#    context = {
#        'title': 'Service',
#        'current_page': 'Service',
#        'banner_image': static('blog/images/my-heart-is-yours.jpg'),
#        'service_image' : static('blog/images/made-it-come-true.jpg'),
#    }
#    return render(request, 'blog/service.html', context)

class ServiceView(TemplateView):
    template_name = 'blog/service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Service'
        context['current_page'] = 'Service'
        context['banner_image'] = static('blog/images/my-heart-is-yours.jpg')
        context['service_image'] = static('blog/images/made-it-come-true.jpg')
        return context