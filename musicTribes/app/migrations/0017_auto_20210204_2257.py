# Generated by Django 3.1.5 on 2021-02-04 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_merge_20210204_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatarurl',
            field=models.CharField(default='https://icon-library.com/images/unknown-person-icon/unknown-person-icon-17.jpg', max_length=500),
        ),
    ]