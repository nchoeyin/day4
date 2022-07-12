import random
print("Welcome to London business men bill picker!")
names = input("Enter the names : ")
listnames = list(names.split(", "))
random_number = random.randint(0, len(listnames)-1)
print(f"{listnames[random_number]} is going to pay")
'''
------------------------------------------------------------------------------------------------------------------------------------
Welcome to London business men bill picker!
Enter the names : Van Dijk, Joe Gomez, Mo Salah, Alison Becker, Trent Arnold, Diego Jota, Jurgenn Klopp
Diego Jota is going to pay

Welcome to London business men bill picker!
Enter the names : Pogba, Martial, Bruno Fernandes, Jadon Sancho, Juan Mata, Harry Maguire, Raphael Varane, David De Gea, Cristiano Ronaldo, Edison Cavani
Martial is going to pay
-------------------------------------------------------------------------------------------------------------------------------------
'''
