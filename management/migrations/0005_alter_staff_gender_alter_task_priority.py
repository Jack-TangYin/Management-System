# Generated by Django 5.1.2 on 2024-11-02 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='gender',
            field=models.SmallIntegerField(choices=[(0, '--Please choose an option--'), (1, 'Male'), (2, 'Female'), (3, 'Transgender'), (4, 'Gender Neutral')], default='--Please choose an option--'),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Urgent', 'Urgent')], default='Medium', max_length=10, verbose_name='Priority'),
        ),
    ]
