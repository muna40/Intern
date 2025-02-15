# Generated by Django 5.1 on 2024-08-31 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_remove_orderplaced_deleted_alter_orderplaced_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='payment_completed',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='payment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.payment'),
        ),
        migrations.AddField(
            model_name='payment',
            name='esewa_order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='esewa_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='esewa_payment_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('On . The .Way', 'On. The.Way'), ('Packed', 'Packed'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], default='Pending', max_length=50),
        ),
    ]
