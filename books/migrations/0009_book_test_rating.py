# Generated by Django 3.0.8 on 2020-08-07 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20200807_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='test_rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='books.Rating'),
        ),
    ]