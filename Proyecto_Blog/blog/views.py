import django.http
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from .serializers import *
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import requests
# Create your views here
#help(django.http.HttpResponse)

def index(request):
    messages = requests.get('http://127.0.0.1:8000/api/posts').json()
    return render(request,'blog/base.html',{'messages':messages})


class PostListInicio(ListView):
    model = Post
    template_name = 'blog/Post_list'
    context_object_name = 'Posts'
    ordering = ['-fecha_posteada']
    paginate_by = 5

class MyCustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 3

class PostListInicioApi(generics.ListAPIView):
    serializer_class = PostListInicioSerializer
    queryset = Post.objects.all()
    pagination_class = MyCustomPagination

    class Meta:
        ordering = ['-fecha_posteada']

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetail(DetailView):
    model = Post
    context_object_name = 'Post'
    template_name = 'blog/Post_detail.html'

class CreatePost(CreateView):
    model = Post
    fields = ['titulo', 'parrafo']
    template_name = 'blog/Post_form.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titulo', 'parrafo']


    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = 'Blog_inicio'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False



def sobre_el_blog(request):
    return render(request, 'blog/sobrenosotros.html', {'title':'Sobre nosotros'})

def contacto(request):
    return render(request, 'blog/contacto.html')