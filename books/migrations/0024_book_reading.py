# Generated by Django 3.0.8 on 2020-08-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0023_rating_sports'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='reading',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
