# Generated by Django 3.0.2 on 2020-01-29 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0005_auto_20200126_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='EndDate',
            field=models.DateField(default=datetime.date(2020, 2, 5)),
        ),
    ]