# Generated by Django 3.0.8 on 2020-08-24 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20200824_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='most_liked_by',
            field=models.CharField(choices=[('girls', 'girls'), ('boys', 'boys'), ('boys and girls', 'bosy and girls')], default='not known yet', max_length=15),
        ),
    ]
