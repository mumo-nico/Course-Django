from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post
# Create your views here.
#dummy data
posts = [
    {
        'author': 'Mumo',
        'title': 'Java',
        'content': 'First Programming',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'Mwia',
        'title': 'JavaScript',
        'content': 'Web devt Programming',
        'date_posted': 'January 2, 2018'
    }
]


def home(request):
    context = {
       # 'posts': posts
       'posts': Post.objects.all()
    }
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post


def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})

#blog -> templates -> blog -> template.html i.e our html files
