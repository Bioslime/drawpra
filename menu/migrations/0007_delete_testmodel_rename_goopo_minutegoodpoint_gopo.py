# Generated by Django 4.0 on 2022-01-05 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_rename_detailgoodpoint_minutegoodpoint'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestModel',
        ),
        migrations.RenameField(
            model_name='minutegoodpoint',
            old_name='goopo',
            new_name='gopo',
        ),
    ]