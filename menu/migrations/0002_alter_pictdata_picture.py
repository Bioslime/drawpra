# Generated by Django 4.0 on 2021-12-31 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictdata',
            name='picture',
            field=models.ImageField(upload_to='pictdata/'),
        ),
    ]