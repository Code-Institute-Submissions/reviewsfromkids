# Generated by Django 3.0.8 on 2020-08-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_auto_20200810_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='age_rating',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
            preserve_default=False,
        ),
    ]
