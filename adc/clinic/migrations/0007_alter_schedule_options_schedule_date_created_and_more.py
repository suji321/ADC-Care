# Generated by Django 4.0.2 on 2022-04-03 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0006_remove_prescription_frequency_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['-date_created']},
        ),
        migrations.AddField(
            model_name='schedule',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='request',
            field=models.TextField(blank=True),
        ),
    ]