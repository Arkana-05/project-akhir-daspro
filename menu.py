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

    perintah = input("Pilih Menu : ")
    if perintah == "1":
        import barang
        barang.show_menu(db)  # Hilangkan print()
    elif perintah == "2":
        import daftarGudang
        daftarGudang.show_data(db)  # Hilangkan print()
    elif perintah == "3":
        import laporan
        laporan.show_data(db)  # Jika ada fungsi show_menu di laporan
    elif perintah == "4":
        import tentangKami
        print(tentangKami)
    elif perintah == "0":
        print("Keluar dari program. Terimakasih😉")
        exit()
    else:
        print("Pilihan Tidak Ada/Tidak ditemukan")


# __name__ igunakan untuk mengeksekusi semua code
# __main__ digunakan untuk sebuah modul dan fungsi
if __name__ == "__main__":
    # PERULANGAN UNTUK MENAMPILKAN MENU
    while(True):
        show_menu()
