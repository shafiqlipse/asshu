from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Article
from .forms import ArticleForm

def article_list(request):
    articles = Article.objects.all().order_by("-created_at")
    return render(request, "articles/article_list.html", {"articles": articles})

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, "articles/article_detail.html", {"article": article})

@login_required
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("article-detail", id=article.id)
    else:
        form = ArticleForm()
    return render(request, "articles/article_form.html", {"form": form})

@login_required
def article_edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.user != article.author:
        return HttpResponseForbidden("You are not allowed to edit this article.")

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect("article-detail", id=article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, "articles/article_form.html", {"form": form})

@login_required
def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    if request.user != article.author:
        return HttpResponseForbidden("You are not allowed to delete this article.")

    if request.method == "POST":
        article.delete()
        return redirect("article-list")
    return render(request, "articles/article_confirm_delete.html", {"article": article})
