from django.shortcuts import render
from .models import News

# Create your views here.

def news(request):

    news_items=News.objects.all()
    return render(request,"News/news.html", {"news":news_items})
