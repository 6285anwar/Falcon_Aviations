# Generated by Django 4.2.1 on 2023-05-23 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falcon_app', '0013_alter_flight_charts_airline_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=240, null=True)),
                ('gender', models.CharField(max_length=240, null=True)),
                ('fullname', models.CharField(max_length=240, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('status', models.CharField(max_length=240, null=True)),
                ('passport_number', models.CharField(max_length=240, null=True)),
                ('seat_no', models.CharField(max_length=240, null=True)),
                ('seat_class', models.CharField(max_length=240, null=True)),
                ('destination', models.CharField(max_length=240, null=True)),
            ],
        ),
    ]
