# Generated by Django 5.1 on 2024-08-31 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_orderplaced_payment_method_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Cancel', 'Cancel'), ('Accepted', 'Accepted'), ('Pending', 'Pending'), ('Delivered', 'Delivered'), ('On . The .Way', 'On. The.Way'), ('Packed', 'Packed')], default='Pending', max_length=50),
        ),
    ]
