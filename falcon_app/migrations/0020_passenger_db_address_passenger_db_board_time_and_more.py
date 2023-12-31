# Generated by Django 4.2.1 on 2023-06-02 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falcon_app', '0019_passenger_db_bag_weight_passenger_db_bags_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger_db',
            name='address',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='passenger_db',
            name='board_time',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='passenger_db',
            name='check_in',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='passenger_db',
            name='company',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='passenger_db',
            name='crew_or_pax',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='passenger_db',
            name='documentexpiry',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='passenger_db',
            name='documentnumber',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='passenger_db',
            name='documenttype',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='passenger_db',
            name='final_destination',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='passenger_db',
            name='issuingcountry',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='passenger_db',
            name='nationality',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='passenger_db',
            name='offload_time',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='passenger_db',
            name='onward_flight',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='passenger_db',
            name='seq_no',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='passenger_db',
            name='special_notes',
            field=models.CharField(max_length=240, null=True),
        ),
    ]
