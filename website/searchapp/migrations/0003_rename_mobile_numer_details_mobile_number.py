# Generated by Django 4.2.7 on 2023-12-03 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0002_details_delete_destinations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='mobile_numer',
            new_name='mobile_number',
        ),
    ]
