# Generated by Django 3.2.3 on 2021-08-28 15:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.PositiveSmallIntegerField(choices=[(2, 'Lost'), (0, 'Available'), (1, 'Borrowed')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.PositiveSmallIntegerField(choices=[(13, 'Triphop'), (3, 'Disco-Polo'), (4, 'Electronic'), (7, 'Pop'), (1, 'Classical'), (6, 'Metal'), (11, 'Rock'), (10, 'Reaggae'), (2, 'Country'), (8, 'R&B'), (0, 'Blues'), (5, 'Jazz'), (12, 'Soundtrack'), (9, 'Rap')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performer', models.CharField(max_length=64, unique=True)),
                ('name_cd', models.CharField(max_length=64)),
                ('publisher', models.CharField(max_length=64)),
                ('year', models.DateField(blank=True, null=True)),
                ('info', models.TextField(default='')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='covers')),
                ('availability', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.availability')),
                ('category_models', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.category')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, default='')),
                ('stars', models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('music', models.ManyToManyField(to='music.Music')),
            ],
        ),
    ]
