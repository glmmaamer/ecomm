# Generated by Django 4.2.13 on 2024-07-07 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_profile_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='address_1',
            new_name='address1',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='address_2',
            new_name='address2',
        ),
    ]
