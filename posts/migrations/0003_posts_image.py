# Generated by Django 4.2 on 2023-11-08 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posts_public_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(default=' ', upload_to='post'),
            preserve_default=False,
        ),
    ]