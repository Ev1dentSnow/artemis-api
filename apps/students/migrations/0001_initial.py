# Generated by Django 3.2.5 on 2021-07-08 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('form', models.IntegerField()),
                ('enrollment_year', models.IntegerField()),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
