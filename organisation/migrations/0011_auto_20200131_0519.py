# Generated by Django 3.0.2 on 2020-01-31 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0010_menu_saturday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='ratings',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
