from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListInicio.as_view(), name='Blog_inicio'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('api/posts', views.PostListInicioApi.as_view(), name='Post-api'),
    path('sobre_nosotros/', views.sobre_el_blog, name='sobre-nosotros'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='Post-Detalle'),
    path('post/new', views.CreatePost.as_view(), name='Post_form'),
    path('post/<int:pk>/update/', views.UpdatePostView.as_view(), name='Post-Update'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='Post-Delete'),
    path('contacto/', views.contacto, name='Contacto' ), #Ejemplo de para que sirve include() en django
]
