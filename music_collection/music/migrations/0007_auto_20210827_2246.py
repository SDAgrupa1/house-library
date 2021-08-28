# Generated by Django 3.2.3 on 2021-08-27 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20210827_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='available',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Available'), (2, 'Lost'), (1, 'Borrowed')], default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(12, 'Soundtrack'), (7, 'Pop'), (3, 'Disco-Polo'), (9, 'Rap'), (0, 'Blues'), (2, 'Country'), (8, 'R&B'), (11, 'Rock'), (13, 'Triphop'), (10, 'Reaggae'), (6, 'Metal'), (4, 'Electronic'), (1, 'Classical'), (5, 'Jazz')], default=0),
        ),
    ]