from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Post

class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class PostListView(ListView):
    template_name: 'post_list.html'
    model = Post

class PostCreateView(CreateView):
    model: Post
    fields: '__all__'
    success_url: reverse_lazy('blog:all')

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model: Post
    fields: '__all__'
    success_url: reverse_lazy('blog:all')

class PostDeleteView(UpdateView):
    model: Post
    fields: '__all__'
    success_url: reverse_lazy('blog:all')