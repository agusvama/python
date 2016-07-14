#booleanos.py
x = 2
print x == 2
print x != 2
print x == 3
print x < 3

nombre = "maldad"
edad = 22

if nombre == "maldad" and edad == 22:
	print "tu nombre es maldad, y tienes 22"

if nombre == "maldad" or nombre == "otro":
	print "tu nombre es maldad u otro"

#el operador in se usa para saber
#si un elemento esta en un arreglo o no
if nombre in ["zak", "obliv"]:
	print "tu nombre es medieval"
else:
	print "tu nombre es, no se"

'''operador is
#sirve para comparar las variables
#pero, solo las variables, no su contenido
'''
x = 1
y = 1
print x == y
print x is y

x = [1,2,3]
y = [1,2,3]
print x == y # Prints out True
print x is y # Prints out False

#operador not
print not False
print not True
print (not False) == False
print (not False) == False
