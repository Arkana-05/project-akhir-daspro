import mysql.connector as mysql

mydb = mysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "python_project_uas",
    port = 3306
)

cursor = mydb.cursor()
cursor.execute(
'''
    CREATE TABLE kas_barang(
    ID INT NOT NULL AUTO_INCREMENT, 
    kode VARCHAR(100) NOT NULL, 
    nama VARCHAR(100) NOT NULL, 
    qty INT NOT NULL, 
    harga INT, 
    total INT, 
    PRIMARY KEY (ID));
''')
mydb.commit()