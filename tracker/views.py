from django.shortcuts import render, redirect
from .models import CurrentBalance, TrackingHistory
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    
    # Initialize
    income = 0
    expense = 0
    current_balance, _ = CurrentBalance.objects.get_or_create(id=1)
    transactions = TrackingHistory.objects.all()
    
    if request.method == "POST":
        # validation
        description = request.POST.get('desc')
        form_amount = request.POST.get('amount')
        
        if not description or not form_amount:
            messages.error(request, "Missing Description or Amount")
            return redirect("/")
        
        amount = float(form_amount)
        if amount == 0:
            print("Amount Cannot be 0")
            messages.error(request, "Amount Cannot be 0")
            return redirect('/')
        
        expense_type = "DEBIT" if (amount<0) else "CREDIT"
        
        TrackingHistory.objects.create(
            current_balance=current_balance,
            amount=amount,
            description=description,
            expense_type=expense_type
        )
        
        current_balance.current_balance += amount
        current_balance.save()
        
        return redirect('/')
    
    for transaction in transactions:
        if transaction.expense_type == "CREDIT":
            income += abs(transaction.amount)
        elif transaction.expense_type == "DEBIT":
            expense += abs(transaction.amount)
            
    context = {
        "transactions": transactions,
        "current_balance": current_balance,
        "income": income,
        "expense": expense
    }
    return render(request, 'index.html', context=context)

def delete_transaction(request, id):
    transaction = TrackingHistory.objects.get(id=id)
    
    if transaction:
        current_balance, _ = CurrentBalance.objects.get_or_create(id=1)
        current_balance.current_balance -= float(transaction.amount)
        current_balance.save()
        transaction.delete()
    else:
        print("Transaction Does not exist")
        
    return redirect("/")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        if not user.exists():
            messages.error(f"user {username} does not exist")
            return redirect("/login/")
        
        user = authenticate(username=username, password=password)
        
        if not user:
            messages.error("Incorrect Password")
            return redirect("/login/")
        
        login(request, user)
        return redirect('/')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "Username already taken")
            return redirect("/signup/")
        
        user = User.objects.create(
            username = username,
            first_name = firstname,
            last_name = lastname
        )
        
        user.set_password(password)
        user.save()
        messages.success(request, "User Created")
        
        login(request, user)
        return redirect("/")
            
    return render(request, 'signup.html')

def logout_view(request):
    pass

