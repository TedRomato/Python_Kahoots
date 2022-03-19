

# Který snippet vrátí výstup?

arr = [50,40,30,20]
'''
Výstup:
20
30
40
50
'''


for i in range(len(arr)):
    index = i
    print(arr[index])


for i in range(arr.length):
    print(arr[i])


for i in range(len(arr)):
    print(arr[0])


last_index = len(arr) - 1
for i in range(len(arr)):
    current_index = last_index - i
    print(arr[i])





# Který řádek vytvoří array s čísly od 1-10?

arr [1,2,3,4,5,6,7,8,9,10]


arr = {1,2,3,4,5,6,7,8,9,10}


arr = 1,2,3,4,5,6,7,8,9,10


arr [1,2,3,4,5,6,7,8,9,10]



# Který řádek přidá na konec arraye číslo 5 
arr = [10,5,16,2,3,45,8]

# odstraní element na indexu 5
arr.pop(5)

# přidá 5 na konec
arr.append(5)

# vrací počet 5
arr.count(5)

# vrací index první 5 
arr.index(5)



# Který snippet vytiskne sudá čísla

arr = [1,2,3,4,5,6,7,8,9]


i = 1

while i < len(arr):
    print(arr[i])
    i += 2

i = 0

while i < len(arr):
    print(arr[i])
    i += 1

i = 0

while i < len(arr):
    print(arr[i])
    i += 2

i = 1

while i < len(arr):
    print(arr[i])
    i += 1



# Který snippet posune všechny auta v cars do prava?

cars = []


for i in range(len(cars)):
    cars[i].x += 5

for i in range(len(cars) - 1):
    cars[i].x += 5

i = 0
while i < len(cars):
    cars[i].x = 5
    i += 1

i = 0
while i <= len(cars):
    cars[i].x += 5
    i += 1


# Který řádek vytiskne 3

arr = [3,2,1]
'''
Výstup:
3
'''

print(len(arr) - 1)
print(arr[1])
print(len(arr) - 1 + arr[2])
print(arr.length)
