# Generated by Django 3.0.1 on 2020-06-21 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0017_invitation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_allowed', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_gallery_permissions', to='event.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_gallery_permissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
