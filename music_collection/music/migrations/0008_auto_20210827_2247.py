# Generated by Django 3.2.3 on 2021-08-27 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20210827_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='available',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Borrowed'), (2, 'Lost'), (0, 'Available')], default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(9, 'Rap'), (2, 'Country'), (5, 'Jazz'), (8, 'R&B'), (4, 'Electronic'), (6, 'Metal'), (7, 'Pop'), (1, 'Classical'), (10, 'Reaggae'), (11, 'Rock'), (12, 'Soundtrack'), (0, 'Blues'), (3, 'Disco-Polo'), (13, 'Triphop')], default=0),
        ),
    ]