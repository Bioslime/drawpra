# Generated by Django 4.0 on 2021-12-31 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_pictdata_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pictdata',
            name='url',
        ),
    ]
