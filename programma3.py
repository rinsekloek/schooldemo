#!/usr/bin/python

# rekensommen :) 

def optellen(a,b):
    return a + b

def aftrekken(a,b):
    return a - b

def vermenigvuldigen(a,b):
    return a * b

def delen(a,b):
    return a / b


print("Kies een rekenmethode")
print("1. Optellen\n")
print("2. Aftrekken\n")
print("3. Vermenigvuldigen\n")
print("4. Delen\n")

while True:
    # vraag de leerling om een rekenmethode te selecteren
    keuze = input("Kies rekenmethode 1, 2, 3 of 4\n")

    # check of de rekenmethode in de opties staat
    if keuze in ('1', '2','3','4'):
        nummer1 = float(input("Toets het eerste getal in: "))
        nummer2 = float(input("Toets het tweede getal in: "))

        if keuze == '1':
            print(nummer1, "+", nummer2, "=", optellen(nummer1,nummer2))
        elif keuze == '2':
            print(nummer1, "-", nummer2, "=", aftrekken(nummer1,nummer2))
        elif keuze == '3':
            print(nummer1, "x", nummer2, "=", vermenigvuldigen(nummmer1,nummmer2))
        elif keuze == '4':
            print(nummer1, "/", nummer2, "=", delen(nummer1,nummer2))

     # check of de leerling een andere calculatie wil maken
        volgende_som = input("wil je nog een som berekenen?: \n")
        if volgende_som == "nee":
         break
else:
  print("incorrect input")
