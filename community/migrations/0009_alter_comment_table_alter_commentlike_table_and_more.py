# Generated by Django 4.1.13 on 2024-12-09 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0008_comment_likes_count_post_likes_count'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comment',
            table='comments',
        ),
        migrations.AlterModelTable(
            name='commentlike',
            table='comment_likes',
        ),
        migrations.AlterModelTable(
            name='like',
            table='likes',
        ),
        migrations.AlterModelTable(
            name='post',
            table='posts',
        ),
    ]
