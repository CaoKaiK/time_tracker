# Generated by Django 2.2.7 on 2019-12-02 18:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_auto_20191201_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_hex',
            field=models.CharField(help_text='Tag Color in Hexadecimal', max_length=6, validators=[django.core.validators.RegexValidator(message='No valid Hex Color code', regex='^([0-9a-fA-F]{6})$')], verbose_name='Color:'),
        ),
    ]
