# Generated by Django 5.1 on 2024-08-31 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_alter_orderplaced_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='payment_method',
            field=models.CharField(choices=[('esewa', 'esewa'), ('Cash On Delivery', 'Cash On Delivery')], default='esewa', max_length=20),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Packed', 'Packed'), ('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Accepted', 'Accepted'), ('On . The .Way', 'On. The.Way')], default='Pending', max_length=50),
        ),
    ]
