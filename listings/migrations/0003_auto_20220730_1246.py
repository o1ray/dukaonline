# Generated by Django 3.2 on 2022-07-30 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20220730_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='garage',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='lot_size',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='sqft',
        ),
    ]
