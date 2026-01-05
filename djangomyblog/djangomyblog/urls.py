# djangomyblog/blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("profile/", views.profile, name="profile"),
    path("signup/", views.signup, name="signup"),

    path("new/", views.new_post, name="new_post"),

    # Detalhe do post
    path("post/<int:id>/", views.post_detail, name="post_detail"),

    # Deletar post
    path("post/<int:id>/delete/", views.delete_post, name="delete_post"),
]
