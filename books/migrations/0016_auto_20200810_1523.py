# Generated by Django 3.0.8 on 2020-08-10 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_remove_book_rated_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='date_of_birth',
            new_name='age_rating',
        ),
    ]