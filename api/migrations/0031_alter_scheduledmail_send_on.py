# Generated by Django 3.2.5 on 2021-09-23 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_alter_scheduledmail_send_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledmail',
            name='send_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 23, 21, 40, 39, 262625)),
        ),
    ]
