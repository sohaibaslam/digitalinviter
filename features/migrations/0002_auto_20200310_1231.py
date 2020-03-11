# Generated by Django 3.0.1 on 2020-03-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='plan',
            field=models.CharField(choices=[('BA', 'Basic Plan'), ('AD', 'Advance Plan'), ('PR', 'Premium Plan')], max_length=2, unique=True),
        ),
    ]