# Generated by Django 3.0.3 on 2022-07-20 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiScam', '0002_stories_emailofscamer'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='scamTitle',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
