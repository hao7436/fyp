# Generated by Django 3.0.3 on 2022-08-21 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('antiScam', '0012_auto_20220821_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addactivites',
            name='toDo',
        ),
    ]