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
                ('availability_choices', models.CharField(choices=[('Available', 'Available'), ('Borrowed', 'Borrowed')], max_length=50, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_choose', models.CharField(choices=[('Blues', 'Blues'), ('Classical', 'Classical'), ('Country', 'Country'), ('Disco-Polo', 'Disco-Polo'), ('Electronic', 'Electronic'), ('Jazz', 'Jazz'), ('Metal', 'Metal'), ('Pop', 'Pop'), ('R&B', 'R&B'), ('Rap', 'Rap'), ('Reaggae', 'Reaggae'), ('Rock', 'Rock'), ('Soundtrack', 'Soundtrack'), ('Triphop', 'Triphop')], max_length=30, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MusicAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cd', models.CharField(max_length=64)),
                ('publisher', models.CharField(max_length=64)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('info', models.TextField(default='')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='covers')),
                ('availability', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.availability')),
                ('category_models', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.category')),
            ],
        ),
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('www', models.URLField(default='https://www.wikipedia.org/', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, default='')),
                ('stars', models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('music', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='music.musicalbum')),
            ],
        ),
        migrations.AddField(
            model_name='musicalbum',
            name='performer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.performer'),
        ),
    ]
