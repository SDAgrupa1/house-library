# Generated by Django 3.2.3 on 2021-08-27 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(9, 'Rap'), (7, 'Pop'), (11, 'Rock'), (2, 'Country'), (6, 'Metal'), (5, 'Jazz'), (4, 'Electronic'), (1, 'Classical'), (12, 'Soundtrack'), (13, 'Triphop'), (10, 'Reaggae'), (0, 'Blues'), (3, 'Disco-Polo'), (8, 'R&B')], default=0),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, default='')),
                ('stars', models.PositiveSmallIntegerField(default=5)),
                ('music', models.ManyToManyField(to='music.Music')),
            ],
        ),
    ]