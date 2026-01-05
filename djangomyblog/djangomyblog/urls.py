from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Autenticação (login, logout, password reset etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # App blog
    path('', include('blog.urls')),
]
