#strings.py

#para darle formato a un string
#se utiliza el %

# %s y %d
nombre = "maldad"
print "hola, %s!!" %nombre
#dentro de %s esta la variable

#para usar 2 o mas argumentos
#usamos una tupla ()
nombre2 = "unee maldad"
edad = 22
print "%s tiene %d years y %s tambien" %(nombre2, edad, nombre)

#cualquier objeto no string
#puede ser formateado usando %s
#
lista = [1, 2, 3]
print "Una lista es como: %s" %lista

#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)

data = ("John", "Doe", 53.44)
format_string = "Hello"
print "Hello %s %s. Your current balance is %.2f$" % data

#un numero puede formatearse como string
#recordar que son objetos en python
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is %s$."
print format_string % data