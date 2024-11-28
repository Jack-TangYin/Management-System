# Generated by Django 5.1.2 on 2024-11-10 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='is_registered',
            field=models.BooleanField(choices=[(True, 'Paid'), (False, 'Unpaid')], default=None, verbose_name='Registration Status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(choices=[(True, 'Paid'), (False, 'Unpaid')], default=None, verbose_name='Payment Status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(verbose_name='Total Amount (£)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Pending'), (2, 'Shipped'), (3, 'Delivered'), (4, 'Canceled'), (5, 'Returned')], default=None, verbose_name='Order Status'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Transgender'), (4, 'Gender Neutral')], default=None),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Urgent', 'Urgent')], default=None, max_length=10, verbose_name='Priority'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('On Hold', 'On Hold'), ('Canceled', 'Canceled')], default=None, max_length=20, verbose_name='Status'),
        ),
    ]