# Generated by Django 3.1.6 on 2021-02-13 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('dog_shelters', '0001_initial'), ('dog_shelters', '0002_auto_20210213_1821')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('intake_date', models.DateTimeField(auto_now_add=True)),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dog_shelters.shelter')),
            ],
        ),
    ]
