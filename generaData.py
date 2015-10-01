#generaData.py
from faker import Faker
f = Faker()

'''for i in xrange(5):
	print
	print "nombre: ", f.name()
	print "usuario: ", f.user_name()
	print "email: ", f.email()
	print "cia: ", f.company()
	print "tel: ", f.phone_number()
	print "direccion: ", f.address()
	print "tarjeta: ", f.credit_card_security_code(card_type=None)
'''
print "INSERT INTO nombres VALUES ("
for i in range (0, 10):
	print "'"+f.name()+"'"+","

print ");"
