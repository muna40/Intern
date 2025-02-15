# Generated by Django 5.1 on 2024-08-31 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_orderplaced_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='payment',
            field=models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Khalti', 'Khalti')], default='Cash On Delivery', max_length=20),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Delivered', 'Delivered'), ('On . The .Way', 'On. The.Way'), ('Pending', 'Pending'), ('Cancel', 'Cancel'), ('Packed', 'Packed')], default='Pending', max_length=50),
        ),
    ]
