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
print("PT DIGITAL IT PROGRAM".center(60))
print("Tahun 2024".center(60))
print(garis) #menampilkan isi dari variable garis
print()


def show_data(db):
    cursor = db.cursor()
    # Mengambil data yang ada di dalam kolom kode, nama dll yang sudah dikelompokkan dan dijumlahkan berdasarkan kode barang
    cursor.execute("SELECT kode, nama, SUM(qty) AS total_qty FROM data_barang GROUP BY kode")
    result = cursor.fetchall()  # Mengambil semua data hasil query

    if cursor.rowcount == 0:  # Jika tidak ada data
        print("Tidak Ada Data yang Ditampilkan")
    else:
        print()
        print("Daftar Gudang".center(60))
        # Header tabel
        headers = ["No", "Kode", "Nama Barang", "Stok"]

        result_index = [(i+1, *row) for i, row in enumerate(result)]  # Tambahkan nomor urut
        # enumerate(result): Menambahkan nomor urut dengan i+1 di awal setiap baris data yang diambil dari result.

        # Tampilkan data dalam bentuk tabel menggunakan tabulate
        print(tabulate(result_index, headers=headers, tablefmt="pretty"))  
show_data(db) #menampilkan fungsi show_data

def detail_data(db):
    cursor = db.cursor()
    
    while True:  # Perulangan untuk mengulang input jika kode tidak ditemukan
        keyword = input("Lihat Detail [Kode] : ")
        
        # Query SQL untuk mencari kode atau nama barang yang sesuai dengan keyword
        sql = "SELECT kode, nama, qty, harga, total FROM data_barang WHERE kode LIKE %s OR nama LIKE %s"
        value = ("%{}%".format(keyword), "%{}%".format(keyword))  # Menggunakan tuple untuk LIKE pada kode dan nama
        
        cursor.execute(sql, value)
        result = cursor.fetchall()  #menampilan semua data dari query sebelumnya

        if cursor.rowcount == 0:  # Jika tidak ada data yang ditemukan
            print("Tidak Ada Data yang Ditampilkan. Silakan coba lagi.")
        else:
            print()
            print("Detail Barang".center(60))

            # Header tabel
            headers = ["Kode", "Nama Barang", "Quantity", "Harga Satuan", "Total"]
            
            # Menampilkan hasil query dalam bentuk tabel menggunakan tabulate
            print(tabulate(result, headers=headers, tablefmt="pretty"))

            # Menjumlahkan total dari semua barang
            total_keseluruhan = sum(int(row[4]) for row in result)  # row[4] adalah kolom 'total' berdasarkan tabel yang ada di database
            
            # Menampilkan total keseluruhan di bawah tabel
            print(f"Total Keseluruhan: Rp.{total_keseluruhan}")
            # perulangan yang akan terus berulang setiap kali detail barang di tampilkan
            while True:
                perintah = input("Kembali ke Menu [Y/T]: ").lower()
                if perintah == "y":
                    import menu
                    menu.show_menu() # menampilkan daftr menu di file menu.py
                    break
                elif perintah == 't':
                    show_data(db)
                    break # dan akan berhenti jika pengguna menginput 't'
                else:
                    print("Kode Salah. Silahkan Coba Lagi")
detail_data(db)
