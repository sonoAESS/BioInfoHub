# Generated by Django 5.1.1 on 2024-11-22 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_status_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
