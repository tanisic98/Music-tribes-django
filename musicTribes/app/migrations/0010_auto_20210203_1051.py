# Generated by Django 3.1.5 on 2021-02-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210201_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatarurl',
            field=models.CharField(max_length=500),
        ),
    ]
