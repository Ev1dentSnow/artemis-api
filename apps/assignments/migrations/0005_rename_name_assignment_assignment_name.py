# Generated by Django 3.2.6 on 2021-08-24 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0004_alter_assignment_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='name',
            new_name='assignment_name',
        ),
    ]
