# Generated by Django 3.0.8 on 2020-08-26 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_book_most_disliked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='gender',
        ),
    ]
