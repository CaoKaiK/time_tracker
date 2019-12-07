# Generated by Django 2.2.7 on 2019-12-06 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_day_is_public_holiday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='end',
            field=models.TimeField(default=datetime.time(9, 0), verbose_name='Working Day End Time'),
        ),
        migrations.AlterField(
            model_name='day',
            name='start',
            field=models.TimeField(default=datetime.time(9, 0), verbose_name='Working Day Start Time'),
        ),
    ]
