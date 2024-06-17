# Generated by Django 5.0.4 on 2024-06-17 00:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental', '0008_alter_car_car_picture_alter_car_problems_picture_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='car_status',
            field=models.CharField(blank=True, choices=[('available', 'Available'), ('broke', 'Broke'), ('unavailable', 'Unavailable'), ('rented', 'Rented')], default='rented', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='parking',
            field=models.CharField(blank=True, choices=[('parking_a', 'Parking A'), ('parking_b', 'Parking B')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'Active'), ('ended', 'Ended')], default='active', max_length=10, null=True),
        ),
    ]