# Generated by Django 3.0.1 on 2020-03-02 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0013_themeimage_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='themeimage',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theme_events', to='event.Event'),
        ),
        migrations.AlterField(
            model_name='themeimage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theme_images', to=settings.AUTH_USER_MODEL),
        ),
    ]
