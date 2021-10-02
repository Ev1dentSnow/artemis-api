# Generated by Django 3.2.6 on 2021-10-01 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.house'),
        ),
    ]
