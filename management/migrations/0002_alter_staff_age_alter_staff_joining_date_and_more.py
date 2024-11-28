# Generated by Django 5.1.2 on 2024-11-01 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='age',
            field=models.IntegerField(verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='joining_date',
            field=models.DateTimeField(verbose_name='Joining Date'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=16, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Salary'),
        ),
    ]