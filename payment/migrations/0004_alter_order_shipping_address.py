# Generated by Django 4.2.13 on 2024-07-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_order_alter_shippingaddress_shipping_email_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.CharField(max_length=1000),
        ),
    ]
