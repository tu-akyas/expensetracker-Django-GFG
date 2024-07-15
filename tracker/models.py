from django.db import models

# Create your models here.

EXPENSE_TYPE_CHOICES = (
    ('CREDIT', 'CREDIT'), 
    ('DEBIT', 'DEBIT')
)

class CurrentBalance(models.Model):
    current_balance = models.FloatField(default=0, editable=False)

    def __str__(self):
        return f"{self.current_balance}"

class TrackingHistory(models.Model):
    current_balance = models.ForeignKey(CurrentBalance, on_delete=models.CASCADE, editable=False)
    amount = models.FloatField(editable=False)
    description = models.CharField(max_length=150)
    expense_type = models.CharField(max_length=10, choices=EXPENSE_TYPE_CHOICES, editable=False)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.description} - {abs(self.amount)} - {self.expense_type}"
    
class RequestLogs(models.Model):
    request_info = models.TextField()
    request_method = models.CharField(max_length=100)
    request_path = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)