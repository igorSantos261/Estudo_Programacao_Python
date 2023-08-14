import mysql.connector

#Conectar ao Banco de Dados#

mydb = mysql.connector.connect(host="localhost",user="root", password="1234", database="pycodebr")

mycursor = mydb.mycursor()
sql= "INSERT INTO clientes (nome, idade, email)VALUES(%s, %s, %s)"
val = [
("Igor", 35, "igor.santos261@gmail.com"),
("Bruna", 34, "bruna.gs.tenorio@gmail.com"),    
("Teste", 20, "teste@gmail.com"),   
]
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "Registros inseridos")