# Generated by Django 3.1.5 on 2021-02-03 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210201_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='url',
            field=models.CharField(max_length=60),
        ),
    ]
