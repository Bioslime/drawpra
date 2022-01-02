# Generated by Django 4.0 on 2022-01-02 16:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_pictdata_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('picture', models.ImageField(default='defo', upload_to='test')),
                ('title', models.CharField(max_length=100)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
