# Generated by Django 3.1.5 on 2021-02-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210203_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='description',
            field=models.TextField(default='Playlist description', max_length=1000),
            preserve_default=False,
        ),
    ]
