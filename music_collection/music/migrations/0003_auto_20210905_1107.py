# Generated by Django 3.2.3 on 2021-09-05 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_performer_spotify'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicalbum',
            name='performer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.performer'),
        ),
        migrations.AlterField(
            model_name='performer',
            name='cd_album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='music.musicalbum'),
        ),
    ]
