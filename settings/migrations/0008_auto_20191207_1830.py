# Generated by Django 2.2.7 on 2019-12-07 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_user_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='weekly_hours',
        ),
        migrations.AddField(
            model_name='user',
            name='normal_end',
            field=models.TimeField(default=datetime.time(17, 0)),
        ),
        migrations.AddField(
            model_name='user',
            name='normal_start',
            field=models.TimeField(default=datetime.time(8, 45)),
        ),
    ]
