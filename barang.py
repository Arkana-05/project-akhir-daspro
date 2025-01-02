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
            kode_barang = input("Kode Barang : ").upper()
            
            while True:  # Loop untuk memastikan nama barang tidak duplikat
                nama_barang = input("Nama Barang : ")

                # Periksa apakah data dengan nama_barang yang sama sudah ada
                cursor = db.cursor()
                cursor.execute("SELECT COUNT(*) FROM data_barang WHERE nama = %s", (nama_barang,))
                # Kode SELECT COUNT(*) FROM data_barang WHERE nama = %s berfungsi untuk menghitung jumlah baris (record) dalam tabel data_barang yang memiliki nama barang tertentu. Misalnya, jika kita mencari nama barang "Lenovo", query ini akan menghitung berapa banyak data barang yang memiliki nama "Lenovo" dalam tabel data_barang. %s adalah tempat untuk nilai yang akan diberikan, misalnya "Lenovo", dalam query tersebut.
                hasil = cursor.fetchone()

                if hasil[0] > 0:
                    print(f"Data dengan Nama Barang '{nama_barang}' sudah ada! Silakan masukkan nama yang berbeda.")
                else:
                    break  # Nama barang unik, keluar dari loop

            # Perulangan untuk memastikan input qty_barang adalah angka
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

            # Menyimpan data ke dalam database
            value = (kode_barang, nama_barang, qty_barang, harga_barang, total)
            sql = "INSERT INTO data_barang (kode, nama, qty, harga, total) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, value)
            db.commit()
            print(f"Data Barang '{nama_barang}' berhasil ditambahkan.")

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
                # Format data untuk kolom Harga Satuan dan Total ke format Rupiah dengan pemisah titik
        formatted_result = [
            [
                row[0], 
                row[1], 
                row[2], 
                row[3],
                f"Rp {int(row[4]):,}".replace(",", ".")   # Format Total
            ] 
            for row in result
            # memproses setiap elemen dalam result satu per satu,
        ]

        # Tampilkan data dalam bentuk tabel menggunakan modul tabulate
        print(tabulate(formatted_result, headers=headers, tablefmt="pretty"))

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
    while True:
        perintah = input("Lanjutkan Update Data? [Y/T] : ").lower()
        if perintah == 'y':
            update_data(db)
        elif perintah == "t":
            print("Terimakasih!")
            show_menu(db)
        else:
            print("Warning!!! Masukkan dalam format [Y/T]")

# HAPUS DATA
def delete_data(db):
    cursor = db.cursor()

   
            # Menampilkan semua data dari code show_data di atas
    show_data(db)
    while True:
        try:
            # Meminta input ID barang
            _id = input("Pilih ID Barang (angka): ")

            # Validasi jika input bukan angka
            if not _id.isdigit():
                raise ValueError("ID harus berupa angka!")

            # Cek apakah ID ada di database
            sql_check = "SELECT * FROM data_barang WHERE id = %s"
            cursor.execute(sql_check, (_id,))
            result = cursor.fetchone()

            if result is None:
                raise ValueError("ID tidak ditemukan di database!")

            # Jika ID valid, hapus data
            sql_delete = "DELETE FROM data_barang WHERE id = %s"
            cursor.execute(sql_delete, (_id,))
            db.commit()
            print("Data berhasil dihapus")

            # Tampilkan data yang tersisa
            show_data(db)
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


# AKSI UNTUK PENCARIAN DATA
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


# AKSI UNTUK EDIT STOK / TAMBAH STOK BARANG (PEMASUKAN STOK BARANG)
def tambah_stok(db):
    cursor = db.cursor()
    # Menambahkan qty baru ke qty yang sudah ada berdasarkan ID barang
    try:
        # Tampilkan daftar barang
        show_data(db)

        # Input ID barang yang akan diedit
        id_barang = int(input("Masukkan ID barang : "))
        
        # Periksa apakah data barang yang dicari ada di database
        cursor.execute("SELECT nama, qty FROM data_barang WHERE id = %s", (id_barang,))
        # %s adalah placeholder dalam query SQL yang digunakan untuk memasukkan nilai secara dinamis saat query dijalankan.
        barang = cursor.fetchone()
        # fetchone() hanya mengambil satu baris dari hasil query

        if barang:
            # Indeks yang digunakan (barang[0], barang[1], dll.) merujuk pada posisi elemen dalam hasil query MySQL (SELECT nama, qty FROM data_barang WHERE id = %s), bukan pada urutan kolom di tabel database.
            print(f"Data Barang ditemukan: {barang[0]}, Stok saat ini: {barang[1]}")
            # f Variabel atau ekspresi Python yang ingin disisipkan dalam string ditempatkan di dalam kurung kurawal {}.
            stok_tambahan = int(input("Tambah stok : "))

            # Update stok barang dengan menambahkan stok tambahan
            # Menggunakan qty = qty + %s untuk menambahkan stok_tambahan ke qty yang sudah ada di database.
            cursor.execute("UPDATE data_barang SET qty = qty + %s WHERE id = %s", (stok_tambahan, id_barang))
            # code qty = qty + %s berfungsi untuk menambahkan nilai tertentu ke kolom qty tanpa mengganti nilai sebelumnya.
            db.commit()
            print(f"Stok barang berhasil ditambahkan! Stok baru: {barang[1] + stok_tambahan}")
        else:
            print("Barang dengan ID tersebut tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Pastikan ID dan stok berupa angka.")

    while True:
        perintah = input("Lanjutkan Tambah Stock [Y/T] : ").lower()
        if perintah == 'y':
            tambah_stok(db)
        elif perintah == "t":
            print("Terimakasih!")
            show_menu(db)
        else:
            print("Warning!!! Masukkan dalam format [Y/T]")

# AKSI UNTUK HAPUS STOK BARANG (PENGELUARAN STOK BARANG)
def hapus_stock(db):
    cursor = db.cursor()
    # Menambahkan stok baru ke stok yang sudah ada berdasarkan ID barang
    try:
        # Tampilkan daftar barang
        show_data(db)

        # Input ID barang yang akan diedit
        id_barang = int(input("Masukkan ID barang : "))
        
        # Periksa apakah barang ada
        cursor.execute("SELECT nama, qty FROM data_barang WHERE id = %s", (id_barang,))
        barang = cursor.fetchone()

        if barang:
            print(f"Data Barang ditemukan: {barang[0]}, Stok saat ini: {barang[1]}")
            stok_tambahan = int(input("Pengeluaran stok : "))

            # Update stok barang dengan menambahkan stok tambahan
            cursor.execute("UPDATE data_barang SET qty = qty - %s WHERE id = %s", (stok_tambahan, id_barang))
            db.commit()
            print(f"Stok barang berhasil dikurangi! Stok terbaru: {barang[1] - stok_tambahan}")
        else:
            print("Barang dengan ID tersebut tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Pastikan ID dan stok berupa angka.")

    while True:
        perintah = input("Lanjutkan Hapus Stock [Y/T] : ").lower()
        if perintah == 'y':
                hapus_stock(db)
        elif perintah == "t":
                print("Terimakasih!")
                show_menu(db)
        else:
            print("Warning!!! Masukkan dalam format [Y/T]")


# Fungsi untuk menggabungkan fungsi tambah dan kurang
def edit_stok(db):
    while(True):
        try:
            #tampilkan menu
            print(baris)
            print("1. Barang Masuk")
            print("2. Barang Keluar")
            print("3. Edit Data")
            print("0. Menu Data Barang")
            print(baris)
            #input ingin menambahkan atau mengurangi
            perintah = int(input("Pilih menu : ")) 
            if perintah == 1:
                tambah_stok(db)
            elif perintah == 2:
                hapus_stock(db)
            elif perintah == 3:
                update_data(db)
            elif perintah == 0:
                show_menu
            else:
                print("Input tidak ditemukan, masukkan sesuai menu")
                continue
            break
        except ValueError:
            print("Warning!!! Format input tidak sesuai")
            continue

# MENAMPILKAN MENU
def show_menu(db):
    while True:  # Perulangan menu utama
        perintah = input("Tampilkan Aksi [Y/T] : ").lower()
        if perintah == 'y':
            print("Aksi".center(60))
            print(baris)
            print("1. Tambah Data")
            print("2. Update Data")
            print("3. Tampilkan Data")
            print("4. Hapus Data")
            print("5. Cari Data")
            print("0. Menu Utama")
            print(baris)

            menu = input("Pilih Aksi : ")

            if menu == "1":
                insert_data(db) #JIKA PILIH 1 MAKA AKAN MUNCUL TAMPILAN UNTUK INSERT DATA DAN SETERUSNYA
            elif menu == "2":
                edit_stok(db)
            elif menu == "3":
                show_data(db)
            elif menu == "4":
                delete_data(db)
            elif menu == "5":
                search_data(db)
            elif menu == "0":
                import menu # JIKA PILIH 0, MAKA AKAN BERALIH PADA FILE MENU.PY
                menu.show_menu()
            else:
                print("Warning!!! Masukkan dalam format [Y/T]")
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
