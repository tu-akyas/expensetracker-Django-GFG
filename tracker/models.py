from django.db import models

# Create your models here.

EXPENSE_TYPE_CHOICES = (
    ('CREDIT', 'CREDIT'), 
    ('DEBIT', 'DEBIT')
)

class CurrentBalance(models.Model):
    current_balance = models.FloatField(default=0)

class TrackingHistory(models.Model):
    current_balance = models.ForeignKey(CurrentBalance, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.CharField(max_length=150)
    expense_type = models.CharField(max_length=10, choices=EXPENSE_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now=True)
    