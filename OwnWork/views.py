from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Article, Account
from .forms import ArticleForm
# Create your views here.
def index(request):
    return render(request, 'index.html', dict(articles=Article.objects.all()[:10]))

def article(request, id):
    return render(request, 'article.html', dict(article=Article.objects.get(id=id)))

def newest(request):
    return render(request, 'index.html', dict(articles=Article.objects.order_by("-published")[:10]))

def create(request):
    if request.method == "GET":
        return render(request, 'form.html', dict(form=ArticleForm(use_required_attribute=False)))
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, use_required_attribute=False)
        if form.is_valid():
            new_article = form.save()
            return redirect('article', id=new_article.id)
        
        err = []
        for field in form.fields.keys():
            if form.has_error(field):
                err.append(field)
                form.fields[field].widget.attrs['class'] = 'error'

        return render(request, 'form.html', dict(form=form, errors=err))
    
