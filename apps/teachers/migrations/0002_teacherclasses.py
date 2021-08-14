# Generated by Django 3.2.5 on 2021-08-14 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_alter_studentclasses_table'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.classes')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher')),
            ],
            options={
                'db_table': 'teacher_classes',
            },
        ),
    ]