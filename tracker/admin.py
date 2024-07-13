from django.contrib import admin
from .models import CurrentBalance, TrackingHistory

# Register your models here.

admin.site.site_header = "Expense Tracker"
admin.site.site_title = "Expense Tracker"

admin.site.register(CurrentBalance)
admin.site.disable_action("delete_selected")

@admin.action(description="Make as Debit")
def make_debit(modeladmin, request, queryset):
    for q in queryset:
        obj = TrackingHistory.objects.get(id=q.id)
        if obj.expense_type == "CREDIT":
            obj.expense_type = "DEBIT"
            obj.amount *= -1
            
            # Multiply by 2 bcz we need remove the credit to reset balance 
            # and make it debit to further match the balance
            obj.current_balance.current_balance += obj.amount * 2 
            obj.current_balance.save()
            obj.save()
            

@admin.action(description="Make as Credit")
def make_credit(modeladmin, request, queryset):
    for q in queryset:
        obj = TrackingHistory.objects.get(id=q.id)
        if obj.expense_type == "DEBIT":
            obj.expense_type = "CREDIT"
            obj.amount *= -1
            
            # Multiply by 2 bcz we need remove the debit to reset balance and make it credit to further match the balance
            obj.current_balance.current_balance += obj.amount * 2
            obj.current_balance.save()
            obj.save()

class TrackingHistoryAdmin(admin.ModelAdmin):
    search_fields = [
        "expense_type",
        "description"
    ]
    
    list_filter = [
        "expense_type"
    ]
    
    list_display = [
        "description",
        "amount",
        "expense_type",
        "current_balance",
        "created_at",
        "display_age"
    ]
    
    actions = [
        make_credit, make_debit
    ]
    def display_age(self, object):
        if object.amount > 0:
            return "+ve"
        else:
            return "-ve"
    

admin.site.register(TrackingHistory, TrackingHistoryAdmin)