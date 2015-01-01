# run this command at the terminal prompt
# python manage.py shell

# within the shell, run the following commands

# (1) Add two books

from books.models import Publisher

p1 = Publisher(name='Apress', address='2855 Telegraph Avenue', city='Berkeley',
               state_province = 'CA', country='U.S.A', website='http://www.apress.com')
p1.save()

# Roughly Translated to SQL =>
#
#   INSERT INTO books_publisher
#       (name, address, city, state_province, country, website)
#   VALUES
#       ('Apress', '2855 Telegraph Avenue', 'Berkeley', 'CA',
#        'U.S.A.','http://www.apress.com')
#

p2 = Publisher(name="O'Reilly", address='10 Fawcett St.', city='Cambridge',
               state_province = 'MA', country='U.S.A', website='http://www.oreilly.com')
p2.save()


# (2) Show the list of books

publisher_list = Publisher.objects.all()

# Roughly Translated to SQL =>
#
#   SELECT id,name, address, city, state_province, country, website
#
#

publisher_list


# (3) Filter data

list = Publisher.objects.filter(name='Apress')

list = Publisher.objects.filter(country="U.S.A")


# (4) Getting a single object
p1 = Publisher.objects.get(name="Apress")


# (5) Updating an object
p1 = Publisher.objects.get(name="Apress")
p1.website = "http://apress.org"
p1.save()

# (6) Deleting an object
p1 = Publisher.objects.get(name="Apress")
p1.delete()


# (7) Show the list of books, order by state asc, desc

publisher_list = Publisher.objects.all().order_by("state_province")

publisher_list = Publisher.objects.all().order_by("-state_province")






