# Generated by Django 4.0.3 on 2022-04-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0013_rename_created_analysis_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='neutral_error',
            field=models.FloatField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='sum_anion',
            field=models.FloatField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='sum_cation',
            field=models.FloatField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='tds_error',
            field=models.FloatField(editable=False, null=True),
        ),
    ]
