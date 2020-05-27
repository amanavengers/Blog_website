from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


def generate_unique_slug(klass, field):
    """
    return unique slug if origin slug is exist.
    eg: `foo-bar` => `foo-bar-1`

    :param `klass` is Class model.
    :param `field` is specific field for title.
    """
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(Slug=unique_slug).exists():
        unique_slug = '%s-%d' % (origin_slug, numb)
        numb += 1
    return unique_slug


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='download.png', upload_to='article_thumbnail')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Slug = models.SlugField(max_length=200, unique=True,default='article.details')

    # python manage.py  makemigrations
    # python manage.py migrate

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + "..."

    def save(self, *args, **kwargs):
        if self.Slug:
            if slugify(self.title) != self.Slug:
                self.Slug = generate_unique_slug(Article, self.title)
        else:
            self.Slug = generate_unique_slug(Article, self.title)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'Slug': self.Slug})
