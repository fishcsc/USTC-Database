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
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View


class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

class AccountPasswordView(View):
    form_class = PasswordForm
    template_name = 'bank_sys/account_password.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        account = get_object_or_404(Account, pk=kwargs['pk'])
        
        if form.is_valid():
            password = form.cleaned_data['password']
            if account.password == password:
                return redirect('bank_sys:account_detail', pk=account.pk)
        
        return render(request, self.template_name, {'form': form, 'error': '密码错误，请重试。'})


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deposits'] = Deposit.objects.filter(account=self.object)
        context['loans'] = Loan.objects.filter(account=self.object)
        return context

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

    def get_queryset(self):
        # 获取 URL 中的 account_id 参数
        account_id = self.request.GET.get('account_id')
        
        # 如果存在 account_id 参数，则只返回该账户的存款记录，否则返回全部存款记录
        if account_id:
            return Deposit.objects.filter(account_id=account_id)
        else:
            return Deposit.objects.all()

class DepositDetailView(DetailView):
    model = Deposit
    template_name = 'bank_sys/deposit_detail.html'

class DepositCreateView(CreateView):
    model = Deposit
    form_class = DepositForm
    template_name = 'bank_sys/deposit_form.html'
    success_url = reverse_lazy('bank_sys:account_list')

class DepositUpdateView(UpdateView):
    model = Deposit
    form_class = DepositForm
    template_name = 'bank_sys/deposit_form.html'
    success_url = reverse_lazy('bank_sys:account_list')

class DepositDeleteView(DeleteView):
    model = Deposit
    template_name = 'bank_sys/deposit_confirm_delete.html'
    success_url = reverse_lazy('bank_sys:account_list')

# Loan Views
class LoanListView(ListView):
    model = Loan
    template_name = 'bank_sys/loan_list.html'

    def get_queryset(self):
        # 获取 URL 中的 account_id 参数
        account_id = self.request.GET.get('account_id')
        
        # 如果存在 account_id 参数，则只返回该账户的存款记录，否则返回全部存款记录
        if account_id:
            return Deposit.objects.filter(account_id=account_id)
        else:
            return Deposit.objects.all()

class LoanDetailView(DetailView):
    model = Loan
    template_name = 'bank_sys/loan_detail.html'

class LoanCreateView(CreateView):
    model = Loan
    form_class = LoanForm
    template_name = 'bank_sys/loan_form.html'
    success_url = reverse_lazy('bank_sys:account_list')

class LoanUpdateView(UpdateView):
    model = Loan
    form_class = LoanForm
    template_name = 'bank_sys/loan_form.html'
    success_url = reverse_lazy('bank_sys:account_list')

class LoanDeleteView(DeleteView):
    model = Loan
    template_name = 'bank_sys/loan_confirm_delete.html'
    success_url = reverse_lazy('bank_sys:account_list')


def calculate_interest(request):
    # 调用数据库函数
    deposit_principal = float(request.GET.get('deposit_principal'))
    deposit_interest_rate = float(request.GET.get('deposit_interest_rate'))
    deposit_interest = calculate_interest_function(deposit_principal, deposit_interest_rate)
    
    # 将结果传递给模板
    return render(request, 'bank_sys/interest_template.html', {'deposit_interest': deposit_interest})

def calculate_interest_function(deposit_principal, deposit_interest_rate):
    # 实现你的数据库函数逻辑
    deposit_interest = deposit_principal * (deposit_interest_rate / 100)
    return deposit_interest