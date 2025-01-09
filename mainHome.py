import mysql.connector
import loginForm

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_project_uas"
)

# variabel untuk menampilkan = sebanyak 60
garis = ("=")*60

if __name__ == "__main__":
    loginForm.login()
