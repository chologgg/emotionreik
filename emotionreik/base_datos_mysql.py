import mysql.connector

config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'ninja2',
  'raise_on_warnings': True
}

conexion = mysql.connector.connect(**config)

### INSERT ###
'''

cursor = conexion.cursor()
nombre= input ("Ingrese su nombre")
mail= input ("ngrese su mail")
edad= int (input ("ngrese su edad"))

add_usuario = ("INSERT INTO prueba "
               "(nombre, mail, edad) "
               "VALUES (%s, %s, %s)")

data_usuario = (nombre, mail, edad)

# Inserto
cursor.execute(add_usuario, data_usuario)

conexion.commit()


### INSERT ###


'''
### SELECT ###

cursor = conexion.cursor()
cursor.execute("SELECT * FROM usuarios")
datos = cursor.fetchall()
print (datos)
conexion.commit()
conexion.close()

#for x in datos:
    #print (x)

### SELECT ###


#conexion.close()



'''
#conexion = mysql.connector.connect(**config)  
#cursor = conexion.cursor()
#cursor.execute('SELECT * FROM pacientes')
#pacientes = cursor.fetchall()
#tupla= pacientes[0]
#id_tipo_dieta=tupla[5]     
#conexion.commit()

cursor = conexion.cursor()
# consulta unida con mas de 1 tabla inner join
cursor.execute('SELECT * FROM pacientes inner join tipo_dieta on pacientes.id_tipo_dieta=tipo_dieta.id_tipo_dieta inner join categoria_hospital on pacientes.id_categoria_hospital=categoria_hospital.id_categoria_hospital')
datos = cursor.fetchall()
print (datos)
conexion.commit()
conexion.close()

'''

