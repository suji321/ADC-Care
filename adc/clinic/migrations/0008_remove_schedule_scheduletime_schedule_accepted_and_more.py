# Generated by Django 4.0.2 on 2022-04-03 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0007_alter_schedule_options_schedule_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='scheduleTime',
        ),
        migrations.AddField(
            model_name='schedule',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='schedule',
            name='accepted_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]