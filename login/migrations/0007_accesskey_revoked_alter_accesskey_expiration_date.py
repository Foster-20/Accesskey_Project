# Generated by Django 5.0.4 on 2024-04-29 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_accesskey_expiration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesskey',
            name='revoked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='accesskey',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 26, 13, 18, 25, 167527, tzinfo=datetime.timezone.utc)),
        ),
    ]
