from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
app_name = 'blog'
urlpatterns = [
    path("", views.index, name="index"),
    path("liste_blog/", views.liste_blog, name="liste_blog"),
    path("blog/<int:blog_id>/", views.blog_details, name="blog_details"),

    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("team/", views.team, name="team"),
    path("gallery/", views.gallery, name="gallery"),

]

#urlpatterns = [
#    path("", views.IndexView.as_view(), name="index"),
#    path("<int:pk>/", views.DetailView.as_view(), name="details"),
#    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
#    path("<int:question_id>/vote/", views.vote, name="vote"),
#]