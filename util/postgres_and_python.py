import psycopg2
# Connect to an existing database
conn = psycopg2.connect("dbname=banco user=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()
cur_cliente = conn.cursor()

#point to the schema
cur.execute("set search_path to banco;")
cur_cliente.execute("set search_path to banco;")
#from table cliente get idCliente
cur_cliente.execute('SELECT "idCliente", "fnacimiento" FROM cliente;')
for i in range(0, 100000): #we have 100000 clientes
    record = cur_cliente.fetchone() #is a tuple
    print record[0],
    print record[1].year

# from table ejecutivo obtain fcontratacion
'''
cur.execute("SELECT * FROM ejecutivo;")
for i in range(0, 148): #number of records in the table
    record = cur.fetchone()
    #(datetime.date(2013, 10, 21),)
    print record[0],      #idEjecutivo
    print record[6].year #fcontratacion
'''
cur.close()
conn.close()
# Execute a command: this creates a new table
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
