# Generated by Django 5.0.4 on 2024-04-29 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_alter_accesskey_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesskey',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 12, 37, 40, 640827, tzinfo=datetime.timezone.utc)),
        ),
    ]
