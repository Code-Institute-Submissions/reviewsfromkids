# Generated by Django 3.0.8 on 2020-08-07 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20200804_1510'),
        ('books', '0006_ratings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, max_length=25, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.Book')),
                ('rated_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserProfile')),
            ],
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
    ]
