# Generated by Django 4.2.1 on 2023-06-06 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falcon_app', '0026_flight_seat_s_10a_flight_seat_s_10b_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger_db',
            name='check_in',
            field=models.CharField(default='0', max_length=240),
        ),
    ]