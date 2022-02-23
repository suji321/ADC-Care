# Generated by Django 3.0.5 on 2022-02-23 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('role', models.CharField(max_length=200, null=True)),
                ('specialisation', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
