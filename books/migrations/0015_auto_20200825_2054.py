# Generated by Django 3.0.8 on 2020-08-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20200825_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='age',
        ),
        migrations.AddField(
            model_name='book',
            name='age_on_book',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
