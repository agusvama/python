#variables.py
#toda variable en python es un objeto
entero = 7
print entero

flotante = 7.0
print flotante
flotante2 = float(7)
print flotante2

#las strings pueden declararse
#con 2 o 1 comillas

string = 'hola'
otraString = "hola3"
print string, otraString

uno = 1
dos = 2
tres = uno + dos
print uno, "+", dos, "=", tres

hola = "hola"
mundo = "mundo"
#uniendo strings
holamundo = hola +" "+ mundo
print holamundo

#se pueden asignar varias en 1 sola linea:
a, b = 3, 4
print "a es", a, "y b es", b

# This will not work!
#print uno + dos + hola 