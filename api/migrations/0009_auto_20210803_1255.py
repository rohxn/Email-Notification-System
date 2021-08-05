# Generated by Django 3.2.4 on 2021-08-03 07:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_scheduledmail_send_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduledmail',
            name='recipients_list',
        ),
        migrations.AlterField(
            model_name='scheduledmail',
            name='send_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 3, 7, 25, 37, 804791, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='MailRecipient',
        ),
    ]