# Generated by Django 2.2.7 on 2019-11-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('act_type', models.CharField(max_length=6, verbose_name='Activity Type')),
                ('act', models.IntegerField(verbose_name='Activity')),
                ('wbs', models.CharField(max_length=24, verbose_name='WBS-Element')),
                ('comment', models.CharField(max_length=20, verbose_name='Comment')),
                ('hours', models.FloatField(verbose_name='Hours')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('total_hours', models.FloatField(verbose_name='Total')),
                ('tg1_hours', models.FloatField(verbose_name='Engineering')),
                ('tg2_hours', models.FloatField(verbose_name='Sales')),
                ('tg3_hours', models.FloatField(verbose_name='Unproductive')),
                ('tg4_hours', models.FloatField(verbose_name='tbd')),
                ('tg5_hours', models.FloatField(verbose_name='Training')),
                ('tg6_hours', models.FloatField(verbose_name='tbd1')),
                ('vac_hours', models.FloatField(verbose_name='Vacation')),
                ('tg7_hours', models.FloatField(verbose_name='Sick')),
                ('tg8_hours', models.FloatField(verbose_name='Research')),
                ('target_hours', models.FloatField(verbose_name='Target')),
                ('diff', models.FloatField(verbose_name='Difference')),
                ('acc_target', models.FloatField(verbose_name='Accumulated Target')),
                ('acc_total', models.FloatField(verbose_name='Accumulated Total')),
                ('is_holiday', models.BooleanField(verbose_name='Public Holiday')),
                ('is_weekend', models.BooleanField(verbose_name='Weekend')),
                ('closed_sap', models.BooleanField(verbose_name='Closed in SAP')),
                ('diff_sap', models.FloatField(verbose_name='Difference to SAP')),
            ],
        ),
    ]
