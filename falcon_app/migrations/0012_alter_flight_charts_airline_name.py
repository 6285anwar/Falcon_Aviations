# Generated by Django 4.2.1 on 2023-05-22 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('falcon_app', '0011_rename_maximum_speed_aircraft_classes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight_charts',
            name='airline_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='falcon_app.airport'),
        ),
    ]