# Generated by Django 3.0.5 on 2020-05-24 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200523_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(default='download.png', upload_to='article_thumbnail'),
        ),
    ]
