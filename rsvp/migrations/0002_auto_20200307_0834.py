# Generated by Django 3.0.1 on 2020-03-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rsvp',
            name='message',
        ),
        migrations.AddField(
            model_name='rsvp',
            name='is_attending',
            field=models.BooleanField(default=True),
        ),
    ]
