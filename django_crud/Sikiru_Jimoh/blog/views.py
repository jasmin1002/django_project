from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    template_name: 'post_list.html'
    model = Post

class PostCreateView(CreateView):
    template_name: 'post_form.html'
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')

class PostDetailView(DetailView):
    template_name: 'post_detail.html'
    model = Post

class PostUpdateView(UpdateView):
    template_name: 'post_form.html'
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')

class PostDeleteView(UpdateView):
    template_name: 'post_form.html'
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')