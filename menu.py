# import modul
import mysql.connector
from reportlab.pdfgen import canvas 
import session

# Koneksi ke database MySQL
db = mysql.connector.connect(
    host="localhost",      
    user="root",           
    password="",           
    database="python_project_uas"
)

# Variabel untuk menampilkan garis
garis = "=" * 60
baris = "-" * 60

# File PDF untuk laporan
pdf_file = "laporan_data_barang.pdf"

# Fungsi untuk menampilkan menu
def show_menu():
    sesi = session.get_session()

    if not sesi:
        print("Tidak ada sesi aktif. Harap login terlebih dahulu.")
        exit()

    role = sesi.get('role')
    username = sesi.get('username')

    print("\nSelamat Datang,", sesi.get('username').capitalize())
    print("Hak Akses Anda:", role)
    print(baris)

    # Tampilkan menu berdasarkan role
    if role == "Admin":
        print("1. Data User")
        print("2. Data Barang")
        print("3. Daftar Gudang")
        print("4. Laporan")
        print("5. Tentang Kami")
        print("0. Keluar")
        valid_menu = {"1", "2", "3", "4", "5", "0"}  # Menu yang valid untuk Admin
    elif role == "User":
        print("2. Data Barang")
        print("3. Daftar Gudang")
        print("5. Tentang Kami")
        print("0. Keluar")
        valid_menu = {"2", "3", "5", "0"}  # Menu yang valid untuk User
    print(baris)

    # Periksa apakah ada data barang di database
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM data_barang")
    data = cursor.rowcount > 0  # True jika ada data
    cursor.close()

    while True:
        perintah = input("Pilih Menu: ")

        # Validasi apakah menu sesuai dengan hak akses
        if perintah not in valid_menu:
            print("Warning!!! Anda tidak dapat membuka akses ke menu ini. Silakan pilih menu yang sesuai.")
            continue  # Kembali meminta input

        # Logika untuk menu valid
        if perintah == "1" and role == "Admin":
            import user
            user.show_menu(db)
        elif perintah == "2":
            import barang
            barang.show_menu(db)
        elif perintah == "3" and data:
            import daftarGudang
            daftarGudang.show_data(db)
        elif perintah == "4" and role == "Admin" and data:
            import laporan
            laporan.show_data(db, pdf_file)
        elif perintah == "5":
            import tentangKami
            tentangKami.cetak()
        elif perintah == "0":
            print("Keluar dari program. Terimakasih 😉")
            exit()
        elif not data and perintah in ("3", "4"):
            print("Data tidak ada, silakan menambah data terlebih dahulu pada menu Data Barang.")
        break


# __name__ igunakan untuk mengeksekusi semua code
# __main__ digunakan untuk sebuah modul dan fungsi
if __name__ == "__main__":
    # PERULANGAN UNTUK MENAMPILKAN MENU
    while(True):
        show_menu()
