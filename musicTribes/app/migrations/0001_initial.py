# Generated by Django 3.1.5 on 2021-01-23 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('creator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('url', models.CharField(max_length=60, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('playlists', models.ManyToManyField(to='app.Playlist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='playlist',
            name='tribe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tribe'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('like', models.BooleanField(default=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('text', models.TextField()),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.playlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='like',
            constraint=models.UniqueConstraint(fields=('user', 'song'), name='user_like'),
        ),
    ]
