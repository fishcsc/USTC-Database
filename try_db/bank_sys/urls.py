from django.urls import path
from .views import (
    CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView,
    StaffListView, StaffDetailView, StaffCreateView, StaffUpdateView, StaffDeleteView,
    AccountListView, AccountDetailView, AccountCreateView, AccountUpdateView, AccountDeleteView,AccountPasswordView,
    DepositListView, DepositDetailView, DepositCreateView, DepositUpdateView, DepositDeleteView,
    LoanListView, LoanDetailView, LoanCreateView, LoanUpdateView, LoanDeleteView
)
from . import views

app_name = 'bank_sys'
urlpatterns = [
    path('', views.home, name='home'),

    # Customer URLs
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/add/', CustomerCreateView.as_view(), name='customer_add'),
    path('customers/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_edit'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),

    # Staff URLs
    path('staff/', StaffListView.as_view(), name='staff_list'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff_detail'),
    path('staff/add/', StaffCreateView.as_view(), name='staff_add'),
    path('staff/<int:pk>/edit/', StaffUpdateView.as_view(), name='staff_edit'),
    path('staff/<int:pk>/delete/', StaffDeleteView.as_view(), name='staff_delete'),

    # Account URLs
    path('accounts/', AccountListView.as_view(), name='account_list'),
    path('accounts/<int:pk>/', AccountPasswordView.as_view(), name='account_password'),
    path('accounts/<int:pk>/detail/', AccountDetailView.as_view(), name='account_detail'),
    path('accounts/add/', AccountCreateView.as_view(), name='account_add'),
    path('accounts/<int:pk>/edit/', AccountUpdateView.as_view(), name='account_edit'),
    path('accounts/<int:pk>/delete/', AccountDeleteView.as_view(), name='account_delete'),

    # Deposit URLs
    path('deposits/', DepositListView.as_view(), name='deposit_list'),
    path('deposits/<int:pk>/', DepositDetailView.as_view(), name='deposit_detail'),
    path('deposits/add/', DepositCreateView.as_view(), name='deposit_add'),
    path('deposits/<int:pk>/edit/', DepositUpdateView.as_view(), name='deposit_edit'),
    path('deposits/<int:pk>/delete/', DepositDeleteView.as_view(), name='deposit_delete'),

    # Loan URLs
    path('loans/', LoanListView.as_view(), name='loan_list'),
    path('loans/<int:pk>/', LoanDetailView.as_view(), name='loan_detail'),
    path('loans/add/', LoanCreateView.as_view(), name='loan_add'),
    path('loans/<int:pk>/edit/', LoanUpdateView.as_view(), name='loan_edit'),
    path('loans/<int:pk>/delete/', LoanDeleteView.as_view(), name='loan_delete'),
]
