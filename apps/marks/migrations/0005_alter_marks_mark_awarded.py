# Generated by Django 3.2.6 on 2021-08-24 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0004_alter_marks_mark_awarded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='mark_awarded',
            field=models.DecimalField(decimal_places=1, max_digits=19),
        ),
    ]
