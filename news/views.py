from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import News

def index(request):
    news = News.objects.all()
    context = {
        'news': news
    }

    return render(request, 'news/index.html')

def news(request):
    return render(request, 'pages/contact.html')

