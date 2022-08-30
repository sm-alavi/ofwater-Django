# Generated by Django 4.0.2 on 2022-03-03 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('well', '0002_well_easting_well_northing_well_utmzone'),
    ]

    operations = [
        migrations.AddField(
            model_name='well',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='well',
            name='long',
            field=models.FloatField(blank=True, null=True),
        ),
    ]