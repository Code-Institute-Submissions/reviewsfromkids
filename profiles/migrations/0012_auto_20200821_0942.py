# Generated by Django 3.0.8 on 2020-08-21 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20200821_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('GIRL', 'girl'), ('BOY', 'boy'), ('UNKNOWN', 'prefer not to say')], max_length=25),
        ),
    ]