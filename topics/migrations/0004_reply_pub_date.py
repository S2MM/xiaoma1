# Generated by Django 2.0.7 on 2018-07-26 15:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0003_auto_20180726_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 26, 15, 17, 12, 327406, tzinfo=utc)),
        ),
    ]
