# Generated by Django 3.0.8 on 2020-08-19 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0024_book_reading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='reading',
        ),
    ]
