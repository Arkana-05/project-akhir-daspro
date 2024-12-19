from tabulate import tabulate
# import modul
import mysql.connector

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


# Fungsi untuk menampilkan data
def show_data(db):
    cursor = db.cursor()
    # MENGAMBIL SEMUA DATA YANG ADA DALAM TABEL DATA_BARANG
    cursor.execute("SELECT kode, nama, qty, harga, total FROM data_barang")
    result = cursor.fetchall()  # Mengambil semua data dari query

    if cursor.rowcount == 0:  # Jika tidak ada data dalam tabel
        print("Tidak Ada Data yang Ditampilkan")
    else:
        print("LAPORAN DATA BARANG".center(60))
        print()
        headers = ["Kode", "Nama Barang", "Quantity", "Harga Satuan", "Total"]
        print(tabulate(result, headers=headers, tablefmt="pretty"))

        # Menjumlahkan total dari semua barang
        total_keseluruhan = sum(int(column[4]) for column in result)  # row[4] adalah kolom 'total' berdasarkan tabel yang ada di database
        
        # Menampilkan total keseluruhan di bawah tabel
        print(f"Total Keseluruhan: Rp.{total_keseluruhan:,.0f}")
# Jalankan fungsi untuk menampilkan data
show_data(db)
