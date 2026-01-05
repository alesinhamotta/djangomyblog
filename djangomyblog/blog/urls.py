from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('new/', views.new_post, name='new_post'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),

    # 👇 
    path('signup/', views.signup, name='signup'),
]
