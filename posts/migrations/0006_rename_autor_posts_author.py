# Generated by Django 4.2 on 2023-11-08 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_posts_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='autor',
            new_name='author',
        ),
    ]
