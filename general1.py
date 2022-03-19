# loops, conditions, function definitions, scope


x = 10
y = 20
if x > y and y != x:
    print("Hello!")

x = 10
y = 20
if x == y and y < x:
    print("Hello!")

x = 10
y = 20
if x < y and y != x:
    print("Hello!")

x = 10
y = 20
if x > y or y == x:
    print("Hello!")



i = 0
while i < 10:
    i += 1
    print(i)


i = 0
while i < 10:
    print(i)
    i += 1


i = 0
while i < 10:
    print(i)
    i -= 1


i = 0
while i > 10:
    i += 1
    print(i)


speed = 1
player = {}

player.speed += 1
player.speed + 1
speed = speed + 1
player.speed = speed + 1







if y >= 14:
    print("Ahoj")
elif y > 12:
    print("Nazdar")
if not y <= 13 :
    print("Adélo")
else :
    print("Karle")



x = int("24")



def change_scale(new_scale):
    global scale
    scale = new_scale

def change_scale(new_scale):
    new_scale = scale

def change_scale():
    global scale
    scale = 12

def change_scale(new_scale)
    global scale
    scale = new_scale


scale = 15

# definice funkce change_scale

change_scale(12)
print(scale) # vytiskne 12





