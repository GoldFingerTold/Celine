from django.urls import path
from MySite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('', views.home, name="Home"),
    path('bio', views.bio, name="Bio"),
    path('escuela', views.escuela, name="Escuela"),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)