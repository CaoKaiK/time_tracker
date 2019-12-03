# Generated by Django 2.2.7 on 2019-12-03 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20191203_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='active',
            field=models.BooleanField(default=True, help_text='Is this Element still active?', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='element',
            name='receiver_order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Receiver Order'),
        ),
    ]
