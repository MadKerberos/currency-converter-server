# Generated by Django 3.0.4 on 2020-11-22 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_remove_bloodtype_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patients',
            old_name='bloodtype',
            new_name='bloodType',
        ),
    ]
