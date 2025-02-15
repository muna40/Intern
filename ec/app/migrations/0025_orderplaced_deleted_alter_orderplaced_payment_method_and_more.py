# Generated by Django 5.1 on 2024-08-31 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_orderplaced_payment_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='payment_method',
            field=models.CharField(choices=[('esewa', 'esewa'), ('Cash On Delivery', 'Cash On Delivery')], default='esewa', max_length=20),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('On . The .Way', 'On. The.Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Accepted', 'Accepted'), ('Packed', 'Packed')], default='Pending', max_length=50),
        ),
    ]
