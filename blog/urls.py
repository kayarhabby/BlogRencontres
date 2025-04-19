from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
app_name = 'blog'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("liste_blog/", views.ListBlogView.as_view(), name="liste_blog"),
    path("<int:pk>/", views.BlogDetailView.as_view(), name="blog_details"),

    path("contact/", views.ContactFormView.as_view(), name="contact"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("team/", views.TeamView.as_view(), name="team"),
    path("gallery/", views.GalleryView.as_view(), name="gallery"),
    path("service/", views.ServiceView.as_view(), name="service"),

]

#urlpatterns = [
#    path("", views.IndexView.as_view(), name="index"),
#    path("<int:pk>/", views.DetailView.as_view(), name="details"),
#    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
#    path("<int:question_id>/vote/", views.vote, name="vote"),
#]