from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article
from django.views.generic import ListView


def home(response):
    articles = Article.objects.all().order_by('date')
    context = {'articles': articles}
    return render(response, 'homepage.html', context)


class PostListView(ListView):
    model = Article
    template_name = 'homepage.html'
    context_object_name = 'articles'
    ordering = ['date']
    paginate_by = 2



def about(response):
    return render(response, 'about.html')
    # return HttpResponse('about')
