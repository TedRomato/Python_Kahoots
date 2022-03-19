# Jakou chybu vyhodí program? 
arr = ["Karel", "Petr", "Klára"] 
print(arr[3])

NameError
IndexError
UnboundLocalError
SyntaxError

# Jakou chybu vyhodí program? 
a = 10
def func()
    print(a) 

IndentationError 
ValueError 
SyntaxError 
UnboundLocalError 

# Jakou chybu vyhodí program? 
from ramdom import randint
random_number = randint(-50,50)
print (random_number) 

ModuleNotFoundError
TypeError
NameError 
SyntaxError 

# Jakou chybu vyhodí program? 
from random import randint
random_number = randint(50,-50)
print (random_number) 

TypeError 
ValueError 
SyntaxError 
NameError 

# Jakou chybu vyhodí program? 
import play
box = play.new_box(x="0", y="0", width="10", height="10")

TypeError
SyntaxError 
IndentationError 
UnboundLocalError 

# Jakou chybu vyhodí program? 
i = 1
while i <= 10:
print(i) 
i += 1

IndentationError 
NameError 
IndexError 
SyntaxError 

ModuleNotFoundError - modul nebyl nalezen (špatně napsané jméno / modul nebyl nainstalovan) 
NameError - zmíněná proměnná nebyla definována
SyntaxError - chyba syntaxe 
IndentationError - chyba odsazení 
UnboundLocalError - lokální proměnná zmíněná před definicí
TypeError - funkce dostala jako argument špatný datový typ
ValueError - funkce dostala jako argument správný datová typ, ale špatnou hodnotu