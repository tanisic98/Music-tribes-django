# Generated by Django 3.1.5 on 2021-02-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20210205_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribe',
            name='logourl',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
