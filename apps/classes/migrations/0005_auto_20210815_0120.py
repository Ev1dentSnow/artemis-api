# Generated by Django 3.2.6 on 2021-08-14 23:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20210815_0101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentclasses',
            old_name='admission_date',
            new_name='start_date',
        ),
        migrations.RemoveField(
            model_name='studentclasses',
            name='graduation_date',
        ),
        migrations.AddField(
            model_name='classes',
            name='graduation_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
