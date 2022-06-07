# Generated by Django 4.0.4 on 2022-06-02 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_alter_stock_max_alter_stock_min'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='max',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='stock',
            name='min',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]