from random import choice

colores = ('blue', 'gray', 'white', 'yellow', 'purple')

for i in range(1, 10):
    #pick a random value from the list: colores
    color = choice(colores)
    print color
