# Generated by Django 3.0.1 on 2020-11-09 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0017_invitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtimeline',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]