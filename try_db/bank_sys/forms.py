from django import forms
from .models import Customer, Staff, Account, Deposit, Loan

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'address']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'gender', 'phone', 'salary', 'level', 'department', 'bank']

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['password', 'balance', 'bank', 'customer']

class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['principal', 'interest_rate', 'deposit_date', 'account']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['principal', 'interest_rate', 'loan_date', 'account']
