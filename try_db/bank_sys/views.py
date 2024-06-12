# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Customer, Staff, Account, Deposit, Loan
from .forms import CustomerForm, StaffForm, AccountForm, DepositForm, LoanForm
from http import client
from locale import currency
from multiprocessing.dummy import current_process
from decimal import Decimal
from re import L
from typing import overload
from django.shortcuts import redirect, render


# Home view
def home(request):
    return render(request, 'bank_sys/home.html')

# Customer Views
class CustomerListView(ListView):
    model = Customer
    template_name = 'bank_sys/customer_list.html'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'bank_sys/customer_detail.html'

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'bank_sys/customer_form.html'
    success_url = reverse_lazy('bank_sys:customer_list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'bank_sys/customer_form.html'
    success_url = reverse_lazy('bank_sys:customer_list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'bank_sys/customer_confirm_delete.html'
    success_url = reverse_lazy('bank_sys:customer_list')

# Staff Views
class StaffListView(ListView):
    model = Staff
    template_name = 'bank_sys/staff_list.html'

class StaffDetailView(DetailView):
    model = Staff
    template_name = 'bank_sys/staff_detail.html'

class StaffCreateView(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = 'bank_sys/staff_form.html'
    success_url = reverse_lazy('bank_sys:staff_list')

class StaffUpdateView(UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = 'bank_sys/staff_form.html'
    success_url = reverse_lazy('bank_sys:staff_list')

class StaffDeleteView(DeleteView):
    model = Staff
    template_name = 'bank_sys/staff_confirm_delete.html'
    success_url = reverse_lazy('bank_sys:staff_list')

# Account Views
class AccountListView(ListView):
    model = Account
    template_name = 'bank_sys/account_list.html'

class AccountDetailView(DetailView):
    model = Account
    template_name = 'bank_sys/account_detail.html'

class AccountCreateView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'bank_sys/account_form.html'
    success_url = reverse_lazy('bank_sys:account_list')

class AccountUpdateView(UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'bank_sys/account_form.html'
    success_url = reverse_lazy('bank_sys:account_list')

class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'bank_sys/account_confirm_delete.html'
    success_url = reverse_lazy('bank_sys:account_list')

# Deposit Views
class DepositListView(ListView):
    model = Deposit
    template_name = 'bank_sys/deposit_list.html'

class DepositDetailView(DetailView):
    model = Deposit
    template_name = 'bank_sys/deposit_detail.html'

class DepositCreateView(CreateView):
    model = Deposit
    form_class = DepositForm
    template_name = 'bank_sys/deposit_form.html'
    success_url = reverse_lazy('bank_sys:deposit_list')

class DepositUpdateView(UpdateView):
    model = Deposit
    form_class = DepositForm
    template_name = 'bank_sys/deposit_form.html'
    success_url = reverse_lazy('bank_sys:deposit_list')

class DepositDeleteView(DeleteView):
    model = Deposit
    template_name = 'bank_sys/deposit_confirm_delete.html'
    success_url = reverse_lazy('bank_sys:deposit_list')

# Loan Views
class LoanListView(ListView):
    model = Loan
    template_name = 'bank_sys/loan_list.html'

class LoanDetailView(DetailView):
    model = Loan
    template_name = 'bank_sys/loan_detail.html'

class LoanCreateView(CreateView):
    model = Loan
    form_class = LoanForm
    template_name = 'bank_sys/loan_form.html'
    success_url = reverse_lazy('bank_sys:loan_list')

class LoanUpdateView(UpdateView):
    model = Loan
    form_class = LoanForm
    template_name = 'bank_sys/loan_form.html'
    success_url = reverse_lazy('bank_sys:loan_list')

class LoanDeleteView(DeleteView):
    model = Loan
    template_name = 'bank_sys/loan_confirm_delete.html'
    success_url = reverse_lazy('bank_sys:loan_list')
