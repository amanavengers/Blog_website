# Generated by Django 3.0.5 on 2020-05-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200517_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='New Delhi', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='New Delhi', max_length=30),
        ),
    ]
