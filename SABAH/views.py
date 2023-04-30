from django.shortcuts import render, HttpResponse
from urllib.parse import unquote

from .models import Article, Author
# Create your views here.

def controller(request):
    articles = Article.objects.all()
    d = {}
    for i in articles:
        if i.Tag not in d.keys():
            d[i.Tag] = 1
        else:
            d[i.Tag] += 1

    if request.GET.get("tag", True) == True:
        return main(request)
    return category(request)

def main(request):
    articles = Article.objects.all()
    d = {}
    for i in articles:
        if i.Tag not in d.keys():
            d[i.Tag] = 1
        else:
            d[i.Tag] += 1
    
    return render(request, "index.html", dict(
        tags=list(sorted(d.items(), key=lambda x:x[1], reverse=True)[:3]),
        articles=articles
    ))

def category(request):
    articles = Article.objects.all()
    d = {}
    for i in articles:
        if i.Tag not in d.keys():
            d[i.Tag] = 1
        else:
            d[i.Tag] += 1
    
    return render(request, "index.html", dict(
        tags=list(sorted(d.items(), key=lambda x:x[1], reverse=True)[:3:]),
        articles=Article.objects.filter(Tag=unquote(request.GET.get("tag")))
    ))

def article(request, id):
    articles = Article.objects.all()
    d = {}
    for i in articles:
        if i.Tag not in d.keys():
            d[i.Tag] = 1
        else:
            d[i.Tag] += 1

    article = articles.filter(id=id)[0]
    article.Views += 1
    article.save()

    return render(request, "article.html", dict(
        tags=list(sorted(d.items(), key=lambda x:x[1], reverse=True)[:3]),
        articles=articles.filter(id=id)
    ))