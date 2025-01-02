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
garis = ("=")*60
baris = ("-")*60

# code untuk menampilkan header

def show_menu():
    print()
    print(garis)    #menampilkan isi dari variable garis
    print("Daftar Menu".center(60)) # menampilkan teks Menu berada di tengah dengan format center
    print(baris)
    print("1. Data Barang")
    print("2. Daftar Gudang")
    print("3. Laporan")
    print("4. Tentang Kami")
    print("0. Keluar")
    print(baris)
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM data_barang")
    if cursor.rowcount == 0 :
        data = False
    else: 
        data = True
    cursor.close()
    perintah = input("Pilih Menu : ")
    if perintah == "1":
        import barang
        barang.show_menu(db)  # Hilangkan print()
    elif perintah == "2" and data:
        import daftarGudang
        daftarGudang.show_data(db)  # Hilangkan print()
    elif perintah == "3" and data:
        import laporan
        laporan.show_data(db)  # Jika ada fungsi show_data di laporan
    elif perintah == "4" :
        import tentangKami
        tentangKami.cetak()
    elif perintah == "0":
        print("Keluar dari program. Terimakasih😉")
        exit()
    elif not data and (perintah == "2" or perintah == "3"):
        print("Data tidak ada, silahkan menambah data terlebih dahulu pada data barang")
    else:
        print("Warning!!! Masukkan dalam format [1/2/3/4/0]")


# __name__ igunakan untuk mengeksekusi semua code
# __main__ digunakan untuk sebuah modul dan fungsi
if __name__ == "__main__":
    # PERULANGAN UNTUK MENAMPILKAN MENU
    while(True):
        show_menu()
