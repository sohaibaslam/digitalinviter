# Generated by Django 3.0.1 on 2020-01-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_event_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='event', max_length=200),
        ),
    ]
