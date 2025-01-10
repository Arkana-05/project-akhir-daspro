import getpass
import mysql.connector
import menu
import session  # Mengimpor modul untuk sesi

# Koneksi ke database
db = mysql.connector.connect(
    host="localhost",  # host database
    user="root",       # username MySQL
    password="",       # password MySQL
    database="python_project_uas"  # Nama database
)

# Variabel untuk menampilkan garis
garis = "=" * 60
baris = "-" * 60

def header():
    print()
    print(garis)
    print("Program Pengadaan Barang".upper().center(60))
    print("PT RADAR IT".center(60))
    print(garis)
    print()

def check_credentials(username, password):
    """Memeriksa username dan password di database."""
    cursor = db.cursor()
    query = "SELECT id, pass FROM user WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result and result[1] == password:
        return result[0]  # Mengembalikan user_id jika login berhasil
    return None

def login():
    """Fungsi utama untuk proses login."""
    while True:
        header()

        # Tanya apakah ingin login atau tidak
        perintah = input("Apakah Anda ingin Login? [Y/T]: ").lower()
        if perintah == "t":
            print("Terimakasih!")
            break
        elif perintah != "y":
            print("WARNING !!! Input dengan Format [Y/T]")
            continue

        print()
        # Proses input username dan password
        user = input("\t User \t\t: ").lower()
        password = getpass.getpass("\t Password \t: ")

        # Validasi username dan password
        user_id = check_credentials(user, password)
        if user_id:
            # Simpan informasi sesi pengguna
            session_data = {
                'id': user_id,
                'username': user,
                'role': "Admin" if user_id.startswith("ADM") else "User"
            }
            session.save_session(session_data)  # Simpan ke sesi
            print(garis)
            print()
            
            # Tampilkan menu berdasarkan role
            menu.show_menu()
            break
        else:
            print("\nMaaf Username atau Password Salah, Silahkan Coba Lagi\n")
