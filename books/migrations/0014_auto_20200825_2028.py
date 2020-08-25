# Generated by Django 3.0.8 on 2020-08-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20200825_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='age_mode',
        ),
        migrations.AddField(
            model_name='book',
            name='not_recommended_by_age',
            field=models.CharField(default='not known yet', max_length=54),
        ),
    ]
