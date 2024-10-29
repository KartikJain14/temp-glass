# Generated by Django 4.2.10 on 2024-09-20 07:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glassbricks', '0010_remove_property_features_property_ac_property_club_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='floor_plan',
            field=models.ImageField(blank=True, null=True, upload_to='property_floor_plan/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])]),
        ),
        migrations.AddField(
            model_name='property',
            name='property_name',
            field=models.CharField(default=property, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='property_images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='property',
            name='videos',
            field=models.FileField(blank=True, null=True, upload_to='property_videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mov'])]),
        ),
    ]