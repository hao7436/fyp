# Generated by Django 3.0.3 on 2022-08-20 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiScam', '0009_addactivites'),
    ]

    operations = [
        migrations.AddField(
            model_name='addactivites',
            name='activitesDate',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
