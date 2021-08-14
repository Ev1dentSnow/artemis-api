# Generated by Django 3.2.5 on 2021-08-14 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('max_marks', models.DecimalField(decimal_places=1, max_digits=3)),
                ('date_assigned', models.DateTimeField()),
                ('date_due', models.DateTimeField()),
            ],
            options={
                'db_table': 'assignments',
            },
        ),
    ]