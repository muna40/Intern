# Generated by Django 5.1 on 2024-08-31 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_orderplaced_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='payment',
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='payment_method',
            field=models.CharField(choices=[('esewa', 'esewa'), ('Cash On Delivery', 'Cash On Delivery')], default='esewa', max_length=20),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Cancel', 'Cancel'), ('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Accepted', 'Accepted'), ('On . The .Way', 'On. The.Way'), ('Packed', 'Packed')], default='Pending', max_length=50),
        ),
    ]
