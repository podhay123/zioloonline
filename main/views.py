from django.shortcuts import render
from main.models import Article


def main(request):
    articles = Article.objects.all()
    print(articles)
    return render(request, "main/index.html", {"articles": articles})


# Create your views here.
