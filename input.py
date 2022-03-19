# Který snippet použijeme pro načtení jména uživatele do proměnné name.

name = input("Zadej jméno: ")
input("Zadej jméno: ") - > name
name = input(Zadej jméno: )
input(name)


# Který program se chová odlišně od ostatních?

name = input("Zadej jméno: ")
answer = "Hello " + name
print(answer)

name = input("Zadej jméno: ")
print("Hello " + name)

print("Hello " + input("Zadej jméno: "))

name = input("Zadej jméno: ")
answer = "Hello " + name
print(name)


# Který program požádá uživatele o jméno, příjmení a pozdraví ho celým jménem? např. "Hello, Filip Werter."

name = input("Zadej jméno: ")
answer = "Hello " + name + "."
print(answer)

input("Zadej jméno: ")
print("Hello " + input + ".")

name = input("Zadej jméno: ")
print("Hello " + name)

print("Hello" + input("Zadej jméno: ") + ".")


# Jaký datový typ vrací funkce input?

String x Integer


# Jaký bude výstup programu když uživatel zadá poprvé "abc" a podruhé "def"?

a = input("First input: ")
b = input("Second input: ")
print(b + b)


# Který program vyhodí chybu?

name = input("Jak se jmenuješ? ")
print("Rád tě poznávám " + name)

entry = input()
print("Uživatel zadal: " + entry)

print(
    input("First input: ") + 
    input("Second input: ")
    )

input("Co máš rád? ")
print("Taky mám rád " + input + ".") 