# Generated by Django 3.2.3 on 2021-08-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20210827_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Classical'), (7, 'Pop'), (11, 'Rock'), (0, 'Blues'), (4, 'Electronic'), (2, 'Country'), (5, 'Jazz'), (13, 'Triphop'), (12, 'Soundtrack'), (6, 'Metal'), (10, 'Reaggae'), (3, 'Disco-Polo'), (8, 'R&B'), (9, 'Rap')], default=0),
        ),
    ]
