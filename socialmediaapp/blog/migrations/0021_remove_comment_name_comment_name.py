# Generated by Django 4.1.3 on 2022-12-07 19:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0020_comment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.ManyToManyField(blank=True, related_name='name', to=settings.AUTH_USER_MODEL),
        ),
    ]