# Generated by Django 4.0.2 on 2022-02-20 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_rename_test_point_test_samplepoint_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]