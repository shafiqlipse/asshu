from django.shortcuts import render, get_object_or_404
from articles.models import Article

# Create your views here.
def home(request):
    articles = Article.objects.all().order_by("-created_at")
    context = {"articles": articles}    
    return render(request, "home/home.html", context)

def about(request):
    context = {}
    return render(request, "home/about.html", context)

def post(request,id):
    article = get_object_or_404(Article, id=id)  # Replace with the actual article ID or slug
    related_articles = Article.objects.exclude(id=id).order_by("-created_at")[:3]  # Get 3 related articles
    context = {
        "article": article,
        "related_articles": related_articles,
    }

    return render(request, "home/post.html", context)
