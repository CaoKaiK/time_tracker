# Generated by Django 2.2.7 on 2019-11-28 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(blank=True, help_text='Customer City', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='postal',
            field=models.CharField(blank=True, help_text='Customer Postal', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='street',
            field=models.CharField(blank=True, help_text='Customer Street', max_length=50, null=True),
        ),
    ]
