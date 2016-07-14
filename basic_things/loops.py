#loops.py

#ciclo for
primos = [2, 3, 5, 7, 11, 13] 

for p in primos:
	print p

print

for x in range(5):
	print x

print 

for x in xrange(5):
	print x

print
# Prints out 3,4,5
for x in xrange(3, 6): # or range(3, 6)
    print x
print
# Prints out 3,5,7
#imprime de 2 en 2
for x in xrange(2, 20, 2): # or range(3, 8, 2)
    print x

print
#ciclo while
cuenta = 0
while cuenta < 5:
	#print "vuelta: %s" %cuenta
	print "vuelta: ", cuenta
	cuenta += 1
print "break"
#rompedor y continuador, jajaja
cuenta = 0
while True:
	print cuenta
	cuenta += 1
	if cuenta >= 5:
		break
print "continue"
for x in xrange(10):
	if x % 2 == 0:
		continue
	print x