from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Jasmine',
        'title': 'Blog post 1',
        'content': 'Blog post first content',
        'date_posted': 'June 18, 2022'
    },
    {
        'author': 'Files',
        'title': 'Blog post 2',
        'content': 'Blog post second content',
        'date_posted': 'June 17, 2022'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')