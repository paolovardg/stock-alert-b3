# Generated by Django 4.0.4 on 2022-06-02 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0013_alter_stock_created_date_alter_stock_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='created_date',
            field=models.DateTimeField(default=True, unique=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='updated_at',
            field=models.DateTimeField(default=True, unique=True),
        ),
    ]
