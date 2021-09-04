# Generated by Django 3.2.3 on 2021-09-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20210904_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performer',
            name='albums',
        ),
        migrations.AddField(
            model_name='performer',
            name='www',
            field=models.URLField(default='https://www.wikipedia.org/', max_length=60),
        ),
    ]
