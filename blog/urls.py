from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("liste_blog/", views.BlogListView.as_view(), name="liste_blog"),
    path("<int:pk>/", views.BlogDetailView.as_view(), name="blog_details"),

    path("contact/", views.ContactFormView.as_view(), name="contact"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("team/", views.TeamListView.as_view(), name="team"),
    path("gallery/", views.GalleryListView.as_view(), name="gallery"),
    path("service/", views.ServiceView.as_view(), name="service"),

]

#urlpatterns = [
#    path("", views.IndexView.as_view(), name="index"),
#    path("<int:pk>/", views.DetailView.as_view(), name="details"),
#    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
#    path("<int:question_id>/vote/", views.vote, name="vote"),
#]