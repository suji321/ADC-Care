# Generated by Django 4.0.2 on 2022-04-11 20:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_delete_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format +919999999999. Up to 10 digits allowed.', regex='^\\+?1?\\d{9,10}$')], verbose_name='Phone'),
        ),
    ]
