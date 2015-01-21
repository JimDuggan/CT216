__author__ = 'jim'

from django.core.management.base import BaseCommand, CommandError
from bank_app.models import Account, Transaction

class Command(BaseCommand):

    def handle(self, *args, **options):
        number = str(args[0])
        print 'Statement for A|C %s' % (number)
        a1 = Account.objects.get(number=number)
        openingBalance = a1.balance
        print 'Current Balance is %.2f' % openingBalance
        print 'List of transactions (one to many)...'
        trans = a1.transaction_set.all()
        for t in trans:
            print 'Date = %s' % str(t.trans_date)
            print 'Transaction Type = %s' % t.tr_type
            print 'Opening Balance = %.2f' % t.openingBalance
            print 'Amount = %.2f' % t.amount
            print 'Closing Balance = %.2f' % t.closingBalance
            print 'Account Number = %s' % t.account.number
            print ''
