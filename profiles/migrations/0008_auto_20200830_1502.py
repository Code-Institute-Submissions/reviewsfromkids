# Generated by Django 3.0.8 on 2020-08-30 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20200830_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, default=None, help_text='Format is year-month-day, e.g. 2010-12-26', null=True),
        ),
    ]
