# Generated by Django 5.0.6 on 2024-06-20 22:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_alter_accesskey_expiration_date_alter_accesskey_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesskey',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 17, 22, 9, 5, 602224, tzinfo=datetime.timezone.utc)),
        ),
    ]