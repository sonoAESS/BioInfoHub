# Generated by Django 5.1.1 on 2024-10-08 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_importants_task_important'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
