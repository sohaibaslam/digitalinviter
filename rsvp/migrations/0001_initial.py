# Generated by Django 3.0.1 on 2020-01-07 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0005_event_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=500, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
