# Generated by Django 4.1 on 2022-08-19 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoolValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BeautyTrue', models.BooleanField()),
                ('HospitalTrue', models.BooleanField()),
                ('TaxiTrue', models.BooleanField()),
                ('HotelTrue', models.BooleanField()),
                ('CafeTrue', models.BooleanField()),
                ('ParkTrue', models.BooleanField()),
                ('Hos24True', models.BooleanField()),
            ],
        ),
    ]
