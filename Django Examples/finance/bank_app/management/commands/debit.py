__author__ = 'jim'

from django.core.management.base import BaseCommand, CommandError
from bank_app.models import Account, Transaction
from decimal import Decimal
from django.utils import timezone

class Command(BaseCommand):

    def handle(self, *args, **options):
        number = str(args[0])
        amount = Decimal(args[1])
        print 'Debited A|C %s with amount of %.2f' % (number, amount)
        a1 = Account.objects.get(number=number)
        openingBalance = a1.balance
        print 'Old Balance is %.2f' % openingBalance
        a1.balance = a1.balance - amount
        a1.save()
        print 'New Balance is %.2f' % a1.balance
        now = timezone.now()
        print 'Time of transaction is %s' % str(now)
        t1 = Transaction(trans_date=now,
                         openingBalance=openingBalance,
                         amount=amount,
                         closingBalance=a1.balance,
                         tr_type="DR",
                         account = a1)
        t1.save()

