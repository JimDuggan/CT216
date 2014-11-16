x = int(input("Please enter a grade: "))

if x < 0:
    print("Grade cannot be negative")
elif x<40:
    print('Grade is E')
elif x < 50:
    print('Grade is D')
elif x < 60:
    print('Grade is C')
elif x < 70:
    print('Grade is B')
elif x <= 100:
    print('Grade is A')
else:
    print('Grade cannot be greater than 100')
