#operadores.py

numero = ((1 + 2) * 3) / 4.0
print numero

#modulo
modulo = 11 % 3
print modulo

#usando operadores con strings
holamundo = "hola" +" "+ "mundo"
print holamundo

muchoshola = "hola " * 10
print muchoshola

#usando operadores con listas
pares = [2, 4, 6, 8]
impares = [1, 3, 5, 7]
todos = pares + impares
todos2 = impares + pares
print todos
print todos2

print [1, 2] * 5

x, y = "x", "y"
lista_x = [x] * 10
lista_y = [y] * 10
print lista_x, lista_y
gran_lista = lista_x + lista_y
print gran_lista
