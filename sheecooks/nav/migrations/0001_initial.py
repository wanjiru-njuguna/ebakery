# Generated by Django 4.2.9 on 2024-03-21 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('date', models.DateField()),
                ('product_name', models.CharField(max_length=100)),
                ('product_serial_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('opening_balance', models.IntegerField(blank=True)),
                ('closing_balance', models.IntegerField(blank=True)),
                ('sales', models.IntegerField(blank=True)),
                ('product_buying_price', models.FloatField(max_length=100)),
                ('product_selling_price', models.FloatField(max_length=100)),
                ('sales_tax', models.FloatField(max_length=20)),
                ('sale_discount', models.FloatField(blank=True)),
                ('photo', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_first_name', models.CharField(max_length=100)),
                ('user_last_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_address', models.CharField(max_length=150)),
                ('profile_pic', models.ImageField(default='default.png', upload_to='images/')),
                ('favorite_items', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='nav.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateField()),
                ('ordering_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nav.user')),
                ('product_ordered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nav.product')),
            ],
        ),
    ]