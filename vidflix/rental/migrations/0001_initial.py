# Generated by Django 3.1.1 on 2020-09-20 17:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('director', models.CharField(max_length=250)),
                ('release_year', models.IntegerField()),
                ('price', models.FloatField()),
                ('image_url', models.TextField()),
                ('description', models.TextField()),
                ('release_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.genre')),
            ],
        ),
    ]
