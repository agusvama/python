#funciones.py

def leppard():
	print "what about heavy rock?"

leppard()

def saludo(nombre, saludo):
	print "Hola, %s, te devuelvo el %s" %(nombre, saludo)

saludo("maldad", "pokemon")

def suma(a, b):
	return a + b

print suma(8, 7)


def lista():
	return "uno", "dos", "tres", "cuatro"

#print lista()

def agregar(numero):
	return "%s es un numero" %numero	

def unir():
	numeros = lista()
	for n in numeros:
		print agregar(n)

unir()	

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

print factorial(4)