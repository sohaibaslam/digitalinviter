# Generated by Django 3.0.1 on 2020-01-21 08:09

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='configuration',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
