# Generated by Django 5.0.4 on 2024-06-15 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental', '0005_client_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'Active'), ('ended', 'Ended')], default='active', max_length=10, null=True),
        ),
    ]
