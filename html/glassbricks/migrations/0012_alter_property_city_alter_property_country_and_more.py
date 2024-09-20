# Generated by Django 4.2.10 on 2024-09-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glassbricks', '0011_property_floor_plan_property_property_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='country',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='landmark',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='locality',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='state',
            field=models.CharField(max_length=255),
        ),
    ]
