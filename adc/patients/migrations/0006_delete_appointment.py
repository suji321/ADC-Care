# Generated by Django 4.0.2 on 2022-04-03 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_alter_appointment_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
