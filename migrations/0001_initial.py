# Generated by Django 3.0.3 on 2022-07-20 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorFname', models.CharField(blank=True, max_length=256)),
                ('authorLname', models.CharField(blank=True, max_length=256)),
                ('authorEmail', models.CharField(blank=True, max_length=256)),
                ('authorNumber', models.CharField(blank=True, max_length=256, null=True)),
                ('scamType', models.CharField(blank=True, max_length=256)),
                ('nameOfScamer', models.CharField(blank=True, max_length=256, null=True)),
                ('contentOfScamer', models.CharField(blank=True, max_length=256, null=True)),
                ('scamDetail', models.TextField()),
            ],
        ),
    ]
