# Generated by Django 2.2.7 on 2019-12-03 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20191203_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='receiver_order',
            field=models.CharField(blank=True, default=None, max_length=6, verbose_name='Receiver Order'),
        ),
    ]