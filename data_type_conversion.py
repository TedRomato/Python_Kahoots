# V proměnné a bude na konci programu řetězec. 

a = 10
a = str(a)

# Který řádek dopíšeme na konec programu níže, abychom vytiskli 100?

a = 50
b = "50"
print(a + b) 
print(a + str(b)) 
print(a + int(b)) 
print(str(a) + str(b)) 


# Na jakou hodnotu němůzeme použít funkci int. 

"55" 
"99.9"
35.2
"two" 


# Vyber program, který načte 2 čísla od uživatele a vytiskne jejich součet.

number1 = input("Zadej první číslo: ") 
number2 = input("Zadej druhé číslo: ") 
number1 = int(number1) 
number2 = int(number2) 
print(number1 + number2) 

number1 = input("Zadej první číslo: ") 
number2 = input("Zadej druhé číslo: ") 
number1 = str(number1) 
number2 = str(number2) 
print(number1 + number2) 

number1 = input("Zadej první číslo: ") 
number2 = input("Zadej druhé číslo: ") 
print(number1 + number2) 


number1 = print("Zadej první číslo: ") 
number2 = print("Zadej druhé číslo: ") 
print(number1 + number2) 


# Který ze snippetů nepatří mezi ostatní (chová se jinak)?

number1 = input("Zadej první číslo: ") 
number2 = input("Zadej druhé číslo: ") 
number1 = int(number1) 
number2 = int(number2) 
print(number1 + number2)

number1 = int(input("Zadej první číslo: ")) 
number2 = int(input("Zadej druhé číslo: ")) 
print(number1 + number2)

print(
    int(input("Zadej první číslo: ")) + 
    int(input("Zadej druhé číslo: "))
    )

number1 = input("Zadej první číslo: ")
number2 = input("Zadej druhé číslo: ")
print(number1 + number2)


# Který program vyhodí chybu?

name = input("Jak se jmenuješ? ")
print("Hello, " + str(name))


birth_year = int(input("Kdy ses narodil? "))
age = 2022 - birth_year
print("Je ti " + str(age) + " let.")


thing = input("Co máš rád? ")
print(thing + " mám taky rád." )


base = input("Zadej stranu čtverce (v cm): ")
base = int(base)
print("Obsah čtverce je " + base*base + " cm2.")