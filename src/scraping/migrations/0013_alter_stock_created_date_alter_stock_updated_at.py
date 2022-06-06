# Generated by Django 4.0.4 on 2022-06-02 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0012_alter_alarmstock_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, unique=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, unique=True),
        ),
    ]
