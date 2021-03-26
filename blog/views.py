from django.shortcuts import render
from .models import Artikel

def index(request):
    context = {
        'articles' : Artikel.objects.all().order_by('-created_date')
    }
    return render(request, 'blog/index.html', context)

def details(request, article_id):
    context = {
        'article' : Artikel.objects.get(id = article_id)
    }
    return render(request, 'blog/details.html', context)

def about(request):

    return render(request, 'blog/about.html')