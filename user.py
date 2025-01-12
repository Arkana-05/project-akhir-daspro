# import modul
import mysql.connector
from tabulate import tabulate
import session 

# Code untuk dapat terkoneksi ke database MySQL
db = mysql.connector.connect(
    host = "localhost",      # host database, biasanya pakai localhost
    user = "root",           # username MySQL, user biasaya root
    password = "",           # password MySQL, password disesuaikan, kalo mac biasanya pw sama dengan user
    database = "python_project_uas"  # Nama database
)

# variabel untuk menampilkan = & - sebanyak 60
garis = "=" * 60
baris = "-" * 60

# code untuk menampilkan header
#code untuk memberi jarak sebanyak 1 kali enter
print() 
print("Program pengadaan barang".upper().center(60)) 
#menampilkan kata program ... dengan huruf kapital semua(upper) dan di setting ada di tengah dengan code center(60), angka 60 di samakan dengan banyaknya garis/baris di atas. 
print("PT RADAR IT".center(60))
print("Tahun 2024".center(60))
print(garis) #menampilkan isi dari variable garis
print()

def insert_data(db):
    while True:
        # Input jumlah data
        while True:
            try:
                jumlah_data = int(input("Jumlah Data: "))
                break
            except ValueError:
                print("Jumlah Data harus berupa angka! Silakan coba lagi.")

        for i in range(jumlah_data):
            print("Data ke " + str(i + 1))
            
            while True:  
                _id = input("ID [ADM1-∞/US1-∞]: ").upper()

                # Validasi format ID
                if not (_id.startswith("ADM") or _id.startswith("US")):
                    print("Role tidak ditemukan. Masukkan ID yang benar (contoh: ADM1 atau US1).")
                    continue  # Kembali ke awal loop

                # Menentukan role berdasarkan prefix ID
                if _id.startswith("ADM"):
                    role = "Admin"
                elif _id.startswith("US"):
                    role = "User"

                # Mengecek apakah ID sudah ada di database
                cursor = db.cursor()
                cursor.execute("SELECT COUNT(*) FROM user WHERE id = %s", (_id,))
                hasil = cursor.fetchone()

                if hasil[0] > 0:
                    print(f"Data dengan ID '{_id}' sudah ada! Silakan masukkan ID yang berbeda.")
                else:
                    break  # ID valid dan tidak ada dalam database

            print(f"ID '{_id}' berhasil digunakan dengan role '{role}'.")

            
            while True:  
                username = input("Username : ").lower()

                cursor = db.cursor()
                cursor.execute("SELECT COUNT(*) FROM user WHERE username = %s", (username,))
                hasil = cursor.fetchone()

                if hasil[0] > 0:
                    print(f"Data dengan Username '{username}' sudah ada! Silakan masukkan username yang berbeda.")
                else:
                    break  

            password = input("Password : ").lower()

            # Menyimpan data ke dalam database
            value = (_id, username, password, role)
            sql = "INSERT INTO user (id, username, pass, role) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, value)
            db.commit()
            print(f"Data User dengan ID '{_id}' berhasil ditambahkan.")

        # Menanyakan apakah ingin menambah data baru
        while True:
            perintah = input("Tambah Data Baru [Y/T]? ").lower()
            if perintah == 't':
                print("Proses selesai. Semua data telah disimpan.")
                return
            elif perintah == 'y':
                break
            else:
                print("Warning!!! Masukkan dalam format [Y/T]")


def show(db):
    cursor = db.cursor()

    cursor.execute("SELECT * FROM user")
    result = cursor.fetchall() #menampilan semua data dari query sebelumnya

    if cursor.rowcount == 0: #jika jumlah data = 0 / tidak ada data dalam tabel, maka  
        print("Data tidak tersedia, silahkan tambah data terlebih dahulu")
    else:
        print("Data User".center(60))
        # Header tabel
        headers = ["ID/Kode","Username", "Password","Role"]
        print(tabulate(result, headers=headers, tablefmt="pretty"))


def delete_data(db):
    cursor = db.cursor()
    show(db)
    while True:
        try:
            # Meminta input ID barang
            _id = input("Pilih ID User : ")

            # Cek apakah ID ada di database
            sql_check = "SELECT * FROM user WHERE id = %s"
            cursor.execute(sql_check, (_id,))
            result = cursor.fetchone()

            if result is None:
                raise ValueError("ID tidak ditemukan di database!")

            # Jika ID valid, hapus data
            sql_delete = "DELETE FROM user WHERE id = %s"
            cursor.execute(sql_delete, (_id,))
            db.commit()
            print("Data berhasil dihapus")

            # Tampilkan data yang tersisa
            show(db)
            break

        except ValueError as e:
            print(f"Error: {e}. Silakan coba lagi.")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            break

    while True:
        perintah = input("Lanjutkan Hapus Data [Y/T] : ").lower()
        if perintah == 'y':
            delete_data(db)
        elif perintah == "t":
            print("Terimakasih!")
            show_menu(db)
        else:
            print("Warning!!! Masukkan dalam format [Y/T]")


# MENAMPILKAN MENU
def show_menu(db):
    
    cursor = db.cursor(buffered = True)
    cursor.execute("SELECT * FROM user")
    if cursor.rowcount == 0:
        data = False
    else:
        data = True
    cursor.close()
    while True:  # Perulangan menu utama
        perintah = input("Tampilkan Aksi [Y/T] : ").lower()
        if perintah == 'y':
            print("Aksi".center(60))
            print(baris)
            print("1. Tambah Data")
            print("2. Hapus Data")
            print("3. Tampilkan Data")
            print("0. Menu Utama")
            print(baris)
            while(True):
                menu = input("Pilih Aksi : ")

                if menu == "1":
                    insert_data(db) #JIKA PILIH 1 MAKA AKAN MUNCUL TAMPILAN UNTUK INSERT DATA DAN SETERUSNYA
                elif (menu == "2"  and data):
                    delete_data(db)
                elif (menu == "3" and data):
                    show(db)
                elif menu == "0":
                    import menu # JIKA PILIH 0, MAKA AKAN BERALIH PADA FILE MENU.PY
                    menu.show_menu()
                elif (not data and (menu == "2")):
                    print("Data tidak tersedia, silahkan tambah data terlebih dahulu")
                    continue
                else:
                    print("Warning!!! Masukkan dalam format [0-3]")
                    continue
                break
        elif perintah == "t":
            print("Terimakasih!")
            perintah = input("Tampilkan Menu Utama [Y/T] : ").lower()
            if perintah == 'y':
                import menu
                menu.show_menu()
            elif perintah == "t":
                print("Terimakasih")
                exit()
            else:
                print("Masukkan dalam format Y/T")
        else:
            print("Warning!! masukkan dalam format Y/T")
    
# __name__ igunakan untuk mengeksekusi semua code
# __main__ digunakan untuk sebuah modul dan fungsi
if __name__ == "__main__":
    # PERULANGAN UNTUK MENAMPILKAN MENU
    while(True):
        show_menu(db)
