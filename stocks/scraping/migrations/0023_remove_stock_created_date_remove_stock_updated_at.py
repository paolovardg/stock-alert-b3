# Generated by Django 4.0.4 on 2022-06-02 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0022_alter_stock_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='updated_at',
        ),
    ]