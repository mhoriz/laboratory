# Generated by Django 4.2.16 on 2025-01-02 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_emergencyhotlines_barangay_official'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Residentss',
            new_name='Resident',
        ),
        migrations.RenameField(
            model_name='requests',
            old_name='resident_id',
            new_name='resident',
        ),
    ]