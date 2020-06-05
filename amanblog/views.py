from django.shortcuts import render
from articles.models import Article
from django.views.generic import ListView


# latest = []
# for i in range(1):
#     latest.append(articles[i])
#
# context = {'articles': articles,
#            'latest': latest,
#            }
#

class PostListView(ListView):
    model = Article
    template_name = 'homepage.html'
    context_object_name = 'articles'
    ordering = ['date']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.all().order_by('date')
        latest = []
        for i in range(2):
            latest.append(articles[i])
        context.update({
            'articles': articles,
            'latest': latest
        })
        return context


def about(response):
    return render(response, 'about.html')
    # return HttpResponse('about')
