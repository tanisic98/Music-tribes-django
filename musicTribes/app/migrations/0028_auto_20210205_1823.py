# Generated by Django 3.1.5 on 2021-02-05 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20210205_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribe',
            name='logourl',
            field=models.CharField(default='https://image.shutterstock.com/image-vector/hand-drawn-tribal-label-textured-260nw-471977746.jpg', max_length=1000),
        ),
    ]