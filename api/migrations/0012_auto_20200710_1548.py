# Generated by Django 3.0.4 on 2020-07-10 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200710_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='bloodType',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('0+', '0+'), ('0-', '0-')], max_length=3),
        ),
    ]