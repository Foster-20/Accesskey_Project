# Generated by Django 5.0.4 on 2024-05-07 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_alter_accesskey_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesskey',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 3, 18, 5, 38, 295672, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='accesskey',
            name='key',
            field=models.CharField(max_length=35, unique=True),
        ),
    ]