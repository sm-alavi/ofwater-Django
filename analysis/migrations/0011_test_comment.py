# Generated by Django 4.0.3 on 2022-03-17 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0010_analysis_equivalent_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]