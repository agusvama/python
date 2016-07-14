from faker import Factory
fake = Factory.create('es_MX')

print "create schema hospital; --mysql"

print "create table medicos"
print "("
print "	cedula		varchar (10) primary key,"
print "	nombrem 	varchar (60),"
print "	apepm 		varchar (60),"
print "	apemm 		varchar (60)"
print ");"

print "create table pacientes"
print "("
print "	rfc		varchar (15) primary key,"
print "	nombrep 	varchar (60),"
print "	apepp 		varchar (60),"
print "	apemp 		varchar (60)"
print ");"

print "create table citas"
print "("	
print "	fecha	    date,"
print "	cedula      varchar (10) references medicos(cedula),"
print "	rfc	    varchar (15) references pacientes(rfc)"
print ");"


for _ in range(0,10):
	cedula_medico= fake.bothify(text="######")
	rfc_paciente=fake.bothify(text="????######??#")

	print "INSERT INTO medicos VALUES ('"+cedula_medico +"','"+fake.first_name()+"','"+fake.last_name()+"','"+fake.last_name()+"');"
	#print "INSERT INTO pacientes VALUES ('"+rfc_paciente+"','"+fake.first_name()+"','"+fake.last_name()+"','"+fake.last_name()+"');"
	#print "INSERT INTO citas VALUES  ('"+fake.date() +"','"+cedula_medico+"','"+rfc_paciente+"');"
