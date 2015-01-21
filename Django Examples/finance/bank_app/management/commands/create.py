__author__ = 'jim'

from django.core.management.base import BaseCommand, CommandError
from bank_app.models import Account

class Command(BaseCommand):

    def handle(self, *args, **options):
        number = str(args[0])
        balance = float(args[1])
        print 'Created A|C %s with opening balance of %.2f' % (number, balance)
        a1 = Account(number=number,balance=balance)
        a1.save()
