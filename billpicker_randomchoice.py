import random
print("Welcome to London business men bill picker!")
names = input("Enter the names : ")
listnames = list(names.split(", "))
print(f"{random.choice(listnames)} is going to pay")
'''
output:
------------------------------------------------------------------------------------------------------------------------------------
Welcome to London business men bill picker!
Enter the names : ng, nn, nc, tt, rw, db, kt
kt is going to
------------------------------------------------------------------------------------------------------------------------------------
'''
