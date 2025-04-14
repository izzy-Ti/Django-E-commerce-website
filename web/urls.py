
from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.front, name='front'),
    path('home/', views.home, name='home'),
    path('products/', include('products.urls')),
    path('about/', views.about, name='about'),
    path('register/', include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
