# Generated by Django 5.1 on 2024-08-31 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_alter_orderplaced_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('esewa', 'esewa')], default='esewa', max_length=20),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Packed', 'Packed'), ('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('Delivered', 'Delivered'), ('On . The .Way', 'On. The.Way')], default='Pending', max_length=50),
        ),
    ]
