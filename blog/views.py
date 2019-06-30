from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'DanRB',
        'title': 'Welcome to the Wedding',
        'content': 'This is where I will put information that is new and relevent to the wedding',
        'date_posted': 'May 5, 2019'
    },
    {
        'author': 'DanRB',
        'title': 'Wedding post 2',
        'content': 'Here is a test placeholder for a second wedding post.',
        'date_posted': 'May 6, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


def welcome(request):
    return render(request, 'blog/welcome.html')
