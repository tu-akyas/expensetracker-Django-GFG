# Generated by Django 5.0.6 on 2024-07-13 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_alter_currentbalance_current_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentbalance',
            name='current_balance',
            field=models.FloatField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='trackinghistory',
            name='amount',
            field=models.FloatField(editable=False),
        ),
        migrations.AlterField(
            model_name='trackinghistory',
            name='current_balance',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='tracker.currentbalance'),
        ),
        migrations.AlterField(
            model_name='trackinghistory',
            name='expense_type',
            field=models.CharField(choices=[('CREDIT', 'CREDIT'), ('DEBIT', 'DEBIT')], editable=False, max_length=10),
        ),
    ]
