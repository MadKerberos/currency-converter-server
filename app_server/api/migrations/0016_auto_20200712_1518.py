# Generated by Django 3.0.4 on 2020-07-12 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20200712_1501'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bloodtype',
            table='api.bloodtype',
        ),
        migrations.AlterModelTable(
            name='patient',
            table='api.patients',
        ),
    ]
