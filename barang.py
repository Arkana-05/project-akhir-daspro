# import modul
import mysql.connector
from tabulate import tabulate
 
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

# TAMBAH DATA KE DATABASE
def insert_data(db):
    # Program utama
    while True:
        # Input jumlah data
        while True:
            try:
                jumlah_data = int(input("Jumlah Data: "))
                break
            except ValueError:
                print("Jumlah Data harus berupa angka! Silakan coba lagi.")

        # Perulangan untuk memasukkan data berdasarkan jumlah yang dimasukkan
        for i in range(jumlah_data):
            print("Data ke "  + str(i + 1))
            kode_barang = input("Kode Barang : ").upper()
            nama_barang = input("Nama Barang : ")
            # perulangan yang akan terus berjalan sebelum menemukan fungsi break
            while True:
                try:
                    qty_barang = int(input("Quantity Barang : "))
                    break
                    # jika inputan yang di tambahkan berupa angka, maka fungsi break akan dijalankan dan perulangan akan otomatis berhenti
                except ValueError:
                    print("Quantity harus berupa angka! Silakan coba lagi.")
                    # jika inputan yang di masukkan bukan angka, maka akan muncul pesan di atas dan perulangan sebelumnya kembali dijalankan sampai fungsi break dijalankan. 

            while True:
                try:
                    harga_barang = int(input("Harga Satuan : "))
                    break
                except ValueError:
                    print("Harga harus berupa angka! Silakan coba lagi.")

            total = harga_barang * qty_barang

            # Menyimpan data ke dalam database
            # variable untuk menampung inputan sebelumnya
            value = (kode_barang ,nama_barang, qty_barang, harga_barang, total)
            # code untuk tambah data kedalam database
            sql = "INSERT INTO data_barang (kode, nama, qty, harga, total) VALUES (%s, %s, %s, %s, %s)"
            # menyimpan data ke database sesuai dengan sql dan value yang telah di buat
            db.cursor().execute(sql, value)
            db.commit() #fungsi untuk menyimpan perubahan ke kedatabase

        # code untuk menanyakan apakah akan menambah data baru atau tidak
        while True:
            perintah = input("Tambah Data Baru [Y/T]? ").lower() #code untuk mengganti huruf menjadi kecil
            if perintah == 't':
                print("Proses selesai. Semua data telah disimpan.")
                return
            elif perintah == 'y':
                break  # Melanjutkan untuk menambah data baru
            else:
                print("Input tidak valid. Masukkan 'Y' untuk menambah data atau 'T' untuk selesai.")



# MENAMPILKAN DATA DARI TABEL DI DATABASE KEDALAM BENTUK TABEL
def show_data(db):
    cursor = db.cursor()
    # MENGAMBIL SEMUA DATA YANG ADA DALAM TABEL DATA_BARANG
    cursor.execute("SELECT * FROM data_barang")
    result = cursor.fetchall() #menampilan semua data dari query sebelumnya

    if cursor.rowcount == 0: #jika jumlah data = 0 / tidak ada data dalam tabel, maka  
        print("Tidak Ada Data yang Ditampilkan")
    else:
        print("Data Barang".center(60))
        # Header tabel
        headers = ["ID","Kode", "Nama Barang", "Quantity", "Harga Satuan", "Total"]
        # Tampilkan data dalam bentuk tabel menggunakan modul tabulate
        print(tabulate(result, headers=headers, tablefmt="pretty"))

# EDIT DATA 
def update_data(db):
    cursor = db.cursor()
    # menampilkan semua data dari code show_data di atas
    show_data(db)
    _id = input("Pilih ID Barang : ")
    
    kode_barang = input("Kode Barang : ")
    nama_barang = input("Nama Barang : ")
    while True:
        try:
            qty_barang = int(input("Quantity Barang : "))
            break
            
        except ValueError:
            print("Quantity harus berupa angka! Silakan coba lagi.")

    while True:
        try:
            harga_barang = int(input("Harga Satuan : "))
            break
        except ValueError:
            print("Harga harus berupa angka! Silakan coba lagi.")

    total = harga_barang * qty_barang
    # nama, qty hahrus sesuai dengan yang ada di tabel
    sql = "UPDATE data_barang SET kode=%s, nama=%s, qty=%s, harga=%s, total=%s WHERE id=%s"
    # untuk value nama variable nya harus sesuai dengan variable input di atas 
    value = (kode_barang, nama_barang, qty_barang, harga_barang, total, _id)
    cursor.execute(sql, value)

    db.commit()
    show_data(db)


def delete_data(db):
    cursor = db.cursor()
    # menampilkan semua data dari code show_data di atas
    show_data(db)
    _id = input("Pilih ID Barang : ")
    
    # nama, qty hahrus sesuai dengan yang ada di tabel
    sql = "DELETE FROM data_barang WHERE id=%s"
    # untuk value nama variable nya harus sesuai dengan variable input di atas 
    value = (_id,)
    cursor.execute(sql, value)

    db.commit()
    print("Data Berhasil dihapus")
    show_data(db)


def search_data(db):
    cursor = db.cursor()
    keyword = input("Masukkan Kata Kunci :")
    sql = "SELECT kode, nama, qty, harga, total FROM data_barang WHERE kode LIKE %s OR nama LIKE %s OR qty LIKE %s OR harga LIKE %s "
    value = ("%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword),)
    # fungsi %% berfungsi untuk menampilkan kata kunci berdasarkan kata kunci yang sudah di inputkan
    cursor.execute(sql, value)
    result = cursor.fetchall()  #menampilan semua data dari query sebelumnya

    if cursor.rowcount == 0: #jika jumlah data = 0 / tidak ada data dalam tabel, maka  
        print("Tidak Ada Data yang Ditampilkan")
    else:
        # Header tabel
        headers = ["Kode", "Nama Barang", "Quantity", "Harga Satuan", "Total"]
        # Tampilkan data dalam bentuk tabel menggunakan modul tabulate
        print(tabulate(result, headers=headers, tablefmt="pretty"))


# MENAMPILKAN MENU
def show_menu(db):
    while True:  # Perulangan menu utama
        perintah = input("Tampilkan Menu [Y/T] : ").lower()
        if perintah == 'y':
            print("Aksi".center(60))
            print(baris)
            print("1. Tambah Data")
            print("2. Tampilkan Data")
            print("3. Edit Data")
            print("4. Hapus Data")
            print("5. Cari Data")
            print("0. Menu Utama")
            print(baris)

            menu = input("Pilih Menu : ")

            if menu == "1":
                insert_data(db) #JIKA PILIH 1 MAKA AKAN MUNCUL TAMPILAN UNTUK INSERT DATA DAN SETERUSNYA
            elif menu == "2":
                show_data(db)
            elif menu == "3":
                update_data(db)
            elif menu == "4":
                delete_data(db)
            elif menu == "5":
                search_data(db)
            elif menu == "0":
                import menu # JIKA PILIH 0, MAKA AKAN BERALIH PADA FILE MENU.PY
                menu.show_menu()
            else:
                print("Pilihan Tidak Ada/Tidak ditemukan")
        else:
            print("Terimakasih!")
            perintah = input("Tampilkan Menu Utama [Y/T] : ").lower()
            if perintah == 'y':
                import menu
                menu.show_menu()
            elif perintah == "t":
                print("Mau kemana sebetulnya toh😥")
                show_menu(db)
            else:
                print("Mau kemana sebetulnya toh😥")
                show_menu(db)
    
# __name__ igunakan untuk mengeksekusi semua code
# __main__ digunakan untuk sebuah modul dan fungsi
if __name__ == "__main__":
    # PERULANGAN UNTUK MENAMPILKAN MENU
    while(True):
        show_menu(db)
