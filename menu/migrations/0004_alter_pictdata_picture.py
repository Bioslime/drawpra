# Generated by Django 4.0 on 2021-12-31 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_remove_pictdata_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictdata',
            name='picture',
            field=models.ImageField(default='defo', upload_to='pictdata/'),
        ),
    ]
