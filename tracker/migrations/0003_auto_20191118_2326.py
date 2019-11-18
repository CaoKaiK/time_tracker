# Generated by Django 2.2.7 on 2019-11-18 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20191118_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='element',
            old_name='project_id',
            new_name='project',
        ),
        migrations.AlterField(
            model_name='element',
            name='act_description',
            field=models.CharField(help_text='Describe the general activity for this WBS', max_length=20),
        ),
    ]
