from django.urls import path
from . import views
urlpatterns = [
    path('perfil/<int:pk>', views.Perfil, name='perfil'),
    path('register', views.Register, name='registro'),
]