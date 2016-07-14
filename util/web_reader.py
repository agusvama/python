import urllib

#link = "http://vasquezmartinezagustin.bitbucket.org/lecturas/pequenio_frances.html"
link = "http://www.thehelloworldprogram.com/es/python-es/por-que-python-deberia-ser-el-primer-lenguaje-de-programacion-que-aprendas/"
f = urllib.urlopen(link) #file handler
contador = 0
palabra_a_buscar = "impresionante"

#use this method, return an array with every line read
lines = f.readlines() #este metodo lee por linea y las devuelve en un arreglo
#now we split the line...
for line in lines:
    #print line
    words = line.split(' ') #separamos palabra por palabra de cada linea
    #print words
    for word in words:
        if word == palabra_a_buscar:
            #print word
            contador = contador + 1

print 'las veces que aparece la palabra %s son: %d' %(palabra_a_buscar, contador)
