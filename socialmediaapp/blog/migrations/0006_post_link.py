# Generated by Django 4.1.3 on 2022-11-25 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.TextField(default='https://www.google.com'),
            preserve_default=False,
        ),
    ]