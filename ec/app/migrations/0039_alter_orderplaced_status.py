# Generated by Django 5.1 on 2024-08-31 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_alter_orderplaced_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Cancel', 'Cancel'), ('Packed', 'Packed'), ('Delivered', 'Delivered'), ('On . The .Way', 'On. The.Way'), ('Pending', 'Pending'), ('Accepted', 'Accepted')], default='Pending', max_length=50),
        ),
    ]
