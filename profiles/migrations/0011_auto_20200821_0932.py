# Generated by Django 3.0.8 on 2020-08-21 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20200820_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('girl', 'girl'), ('boy', 'boy'), ('unknown', 'prefer not to say')], max_length=25),
        ),
    ]