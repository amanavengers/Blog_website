from django.shortcuts import render, redirect
from .models import Article
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import render
from articles.models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

# example of default view
def article_list(request):
    articles = Article.objects.all().order_by('date')
    context = {'articles': articles}
    return render(request, 'articles/article_list.html', context)


# example of class based view (list type)
class Post_Article_ListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    ordering = ['date']


def article_detail(request, Slug):
    article = Article.objects.get(Slug=Slug)
    context_detail = {'article': article}
    return render(request, 'articles/article_detail.html', context_detail)


class PostDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    slug_field = 'Slug'
    slug_url_kwarg = 'Slug'


@login_required
def article_create(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("articles:list")
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {"form": form})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'articles/article_create.html'
    fields = ['title', 'body', 'thumbnail']
    slug_field = 'Slug'
    slug_url_kwarg = 'Slug'

    def form_valid(self, form):
        form.instance.author = self.request.user
        if 'thumbnail' in self.request.FILES:
            form.instance.thumbnail = self.request.FILES['thumbnail']
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'articles/article_create.html'
    fields = ['title', 'body', 'thumbnail']
    slug_field = 'Slug'
    slug_url_kwarg = 'Slug'

    def form_valid(self, form):
        form.instance.author = self.request.user
        if 'thumbnail' in self.request.FILES:
            form.instance.thumbnail = self.request.FILES['thumbnail']
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin,DeleteView):
    model = Article
    success_url = '/'
    template_name = 'articles/article_delete.html'
    slug_field = 'Slug'
    slug_url_kwarg = 'Slug'

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False