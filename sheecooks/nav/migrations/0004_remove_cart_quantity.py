# Generated by Django 4.2.9 on 2024-04-15 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nav', '0003_alter_cart_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
    ]
