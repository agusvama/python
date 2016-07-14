#clases.py

class MyClase:

	variable = "blah"

	def function(self):
		print "Este es un mensaje dentro de la clase"

objeto = MyClase()

print objeto.variable
#GET
objeto2 = MyClase()
objeto2.variable = "yackity"
#SET
print objeto.variable
print objeto2.variable

objeto.function()
