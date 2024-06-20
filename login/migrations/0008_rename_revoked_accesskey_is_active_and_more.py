# Generated by Django 5.0.4 on 2024-04-29 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_accesskey_revoked_alter_accesskey_expiration_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accesskey',
            old_name='revoked',
            new_name='is_active',
        ),
        migrations.AlterField(
            model_name='accesskey',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 26, 13, 21, 34, 828998, tzinfo=datetime.timezone.utc)),
        ),
    ]
