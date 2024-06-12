from asyncio import constants
from datetime import date
from locale import currency
from operator import mod
from turtle import Turtle
# from tkinter import CASCADE
from django.db import models
from django.forms import CharField, DecimalField
from pymysql import NULL


# # Create your models here.






# # new

# # class Question(models.Model):
# #     question_text = models.CharField(max_length=200)
# #     pub_date = models.DateTimeField("date published")


# # class Choice(models.Model):
# #     question = models.ForeignKey(Question, on_delete=models.CASCADE)
# #     choice_text = models.CharField(max_length=200)
# #     votes = models.IntegerField(default=0)


class Department(models.Model):
    # department_id = models.CharField(max_length=20, primary_key=True)
    department_name = models.CharField(max_length=100)
    def __str__(self):
        return self.department_name

    # class Meta:
    #     db_table = "Department"

class Bank(models.Model):
    bank_name = models.CharField(max_length=100)
    total_assets = models.DecimalField(max_digits=15, decimal_places=2)
    def __str__(self):
        return self.bank_name
    # class Meta:
    #     db_table = "Bank"

class Customer(models.Model):
    # customer_id = models.CharField(max_length=18, primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    # class Meta:
    #     db_table = "Customer"

class Account(models.Model):
    # account_id = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

    # class Meta:
    #     db_table = "Account"

class Loan(models.Model):
    # loan_id = models.CharField(max_length=20, primary_key=True)
    principal = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    loan_date = models.DateField(default=date.today)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='loans')
    def __str__(self):
        return str(self.id)
    # class Meta:
    #     db_table = "Loan"

class Deposit(models.Model):
    # deposit_id = models.CharField(max_length=20, primary_key=True)
    principal = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    deposit_date = models.DateField(default=date.today)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
    # class Meta:
    #     db_table = "Deposit"

class Staff(models.Model):
    # staff_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=11, unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    # class Meta:
    #     db_table = "Staff"
