#strings2.py

#algunas operaciones con strings

gato = "gato azul"
#imprimir longitud de la cadena
print len(gato)
#imprimir el indice donde esta tal letra
print gato.index("o")
print gato.index("g")
print gato.index("l")
print gato.index("a")
#este metodo solo sirve para la primera
#letra en la string, notar que hay 2 A's

#contar las letras que hay en una string
print gato.count("a")
print gato.count("z")
#imprime desde 2 hasta 7
#print string[a:b]
# >=a, <b
print gato[2:8]
#2nd character from the end
print gato[-2:8]

#convertir a mayus y minus
#hace una nueva string, no modifica la anterior
print gato.upper()
print gato
print gato.lower()

#saber si la cadena empieza o termina con algo
print gato.startswith("gato")
print gato.endswith("xxx")

#separar la cadena en partes
#de acuerdo al separador que pasemos como argumento
gato2 = "ga;to; az;ul"
palabras = gato.split(" ")
print palabras
palabras = gato2.split(";")
print palabras