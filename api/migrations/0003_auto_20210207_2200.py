# Generated by Django 3.1.2 on 2021-02-07 14:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_travelreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelreview',
            name='username',
            field=models.ForeignKey(db_column='username', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='travelreview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 7, 22, 0, 47, 383580)),
        ),
    ]