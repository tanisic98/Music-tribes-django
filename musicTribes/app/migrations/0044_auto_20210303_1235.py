# Generated by Django 3.1.5 on 2021-03-03 11:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_auto_20210303_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_duration',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 3, 11, 35, 10, 941973, tzinfo=utc)),
        ),
    ]
