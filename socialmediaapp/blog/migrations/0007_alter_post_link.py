# Generated by Django 4.1.3 on 2022-11-25 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.TextField(max_length=200),
        ),
    ]