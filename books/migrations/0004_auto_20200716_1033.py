# Generated by Django 3.0.8 on 2020-07-16 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20200716_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_added',
            field=models.DateField(),
        ),
    ]