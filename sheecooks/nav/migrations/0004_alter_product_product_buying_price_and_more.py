# Generated by Django 4.2.9 on 2024-03-31 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nav', '0003_toppicks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_buying_price',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_selling_price',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
