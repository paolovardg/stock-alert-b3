# Generated by Django 4.0.4 on 2022-06-07 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0035_alter_alarmstock_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
