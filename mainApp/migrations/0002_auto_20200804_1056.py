# Generated by Django 3.0.8 on 2020-08-04 05:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 4, 10, 56, 2, 917234), verbose_name='date published'),
        ),
    ]
