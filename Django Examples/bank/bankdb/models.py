from django.db import models

# Create your models here.

class Account(models.Model):
    number = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return self.number

class Transaction(models.Model):
    trans_date = models.DateField()
    openingBalance = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    closingBalance = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(Account)  # many to one link


