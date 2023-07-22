from django.urls import path
from users.views import perfil, register
urlpatterns = [
    path('perfil/<int:pk>', perfil, name='perfil'),
    path('register', register, name='registro'),
]