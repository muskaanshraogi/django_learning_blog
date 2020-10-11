from django.shortcuts import render

posts = [
    {
        'title': 'Blog 1',
        'author': 'Muskaan Shraogi',
        'content': 'Welcome to my blog.',
        'postedOn': 'October 10, 2020'
    },
    {
        'title': 'Blog 2',
        'author': 'Caroline Forbes',
        'content': 'Seriously!??',
        'postedOn': 'October 9, 2020'
    }
]

def home(request):
    context = {
        'title': 'Muskaan\'s Blog',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
