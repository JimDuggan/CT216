__author__ = 'jim'

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    def credit(self):
        print("Credit")

    def handle(self, *args, **options):
        self.stdout.write('Test Command...')
        print("Hello World...")
        print(args)
        print(args[0])
        for a in args:
            print(a)
            if a=="credit":
                self.credit()