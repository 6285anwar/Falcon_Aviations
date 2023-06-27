# Generated by Django 4.2.1 on 2023-05-22 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falcon_app', '0009_flight_charts_arrival_airport_to_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, null=True)),
                ('manufacturer', models.CharField(max_length=240, null=True)),
                ('model', models.CharField(max_length=240, null=True)),
                ('registration_number', models.CharField(max_length=240, null=True)),
                ('year_of_manufacture', models.CharField(max_length=240, null=True)),
                ('seating_capacity', models.CharField(max_length=240, null=True)),
                ('maximum_speed', models.CharField(max_length=240, null=True)),
                ('fuel_capacity', models.CharField(max_length=240, null=True)),
                ('engine_type', models.CharField(max_length=240, null=True)),
                ('status', models.CharField(max_length=240, null=True)),
                ('flight_status', models.CharField(max_length=240, null=True)),
            ],
        ),
    ]
