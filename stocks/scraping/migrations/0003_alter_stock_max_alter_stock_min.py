# Generated by Django 4.0.4 on 2022-06-02 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_alter_stock_max_alter_stock_min'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='max',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='stock',
            name='min',
            field=models.CharField(max_length=250),
        ),
    ]