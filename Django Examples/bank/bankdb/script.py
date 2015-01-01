__author__ = 'jim'

from bankdb.models import Transaction, Account

a1 = Account(number='123456',balance=0.0)
tr = Transaction(trans_date='2014-01-01',openingBalance=0.0,amount=100.0,closingBalance=100.0,account=a1)
tr1 = Transaction(trans_date='2014-01-01',openingBalance=100.0,amount=100.0,closingBalance=200.0,account=a1)


a1.save()
tr.save()


# get all the transactions for an account - one to many link
# this is a reverse action on the foreign key defined in transaction

tr_list = a1.transaction_set.all()

tr = tr_list[0]

# find the account for a given (1st) transaction (many to one link)
ac1 = tr.account