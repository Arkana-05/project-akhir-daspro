# variabel untuk menampilkan = & - sebanyak 60
garis = ("=")*60
baris = ("-")*60

# code untuk menampilkan header
print() 
print("Program pengadaan barang".upper().center(60)) 
#menampilkan kata program ... dengan huruf kapital semua(upper) dan di setting ada di tengah dengan code center(60), angka 60 di samakan dengan banyaknya garis/baris di atas. 
print("PT RADAR IT".center(60))
print("Tahun 2024".center(60))
print(garis) #menampilkan isi dari variable garis
print()

print("Kelompok Daspro".center(60))
print()
print("Ketua    : Dias Havits / 19241041")
print("Anggota  : Muhammad Ramdhan M. / 19241129")
print("         : Anggraini S. / 19240838")
print("         : Arka N. / 19241186")
print("         : Muhammad Arya D.A / 19241012")
print()

def show_data():
    while True:
        show = input("Tampilkan Data Team [Y/T] : ").lower()
        if show == 'y':
            print("Nama\t: Dias H.")
            print("NIM\t: 19241041")
            print("Prodi\t: Sistem Informasi")
            print("Kelas\t: 19.1B.13")
            print("Posisi\t: Ketua")
            print()
            print("Nama\t: Muhammad Ramdhan Maulana")
            print("NIM\t: 19241129")
            print("Prodi\t: Sistem Informasi")
            print("Kelas\t: 19.1B.13")
            print("Posisi\t: Anggota")
            print()
            print("Nama\t: Anggraini Suprapto")
            print("NIM\t: 19240838")
            print("Prodi\t: Sistem Informasi")
            print("Kelas\t: 19.1B.13")
            print("Posisi\t: Anggota")
            print()
            print("Nama\t: Arka N.")
            print("NIM\t: 19241186")
            print("Prodi\t: Sistem Informasi")
            print("Kelas\t: 19.1B.13")
            print("Posisi\t: Anggota")
            print()
            print("Nama\t: Muhammad Arya D.A")
            print("NIM\t: 19241012")
            print("Prodi\t: Sistem Informasi")
            print("Kelas\t: 19.1B.13")
            print("Posisi\t: Anggota")
            print()
            
            back = input("Kembali ke Menu [Y/T] : ").lower()
            if back == 'y':
                import menu
                menu.show_menu()
            elif back == "t":
                print("Terimakasih")
                show_data()
            else:
                print("Pilihan Tidak Ada/Tidak ditemukan")
                show_data()
                
        elif show == "t":
            print("Terimakasih")
            back = input("Kembali ke Menu [Y/T] : ").lower()
            if back == 'y':
                import menu
                menu.show_menu()
            elif back == "t":
                print("Mau kemana sebetulnya toh😥")
                show_data()
            else:
                print("Pilihan Tidak Ada/Tidak ditemukan")
                show_data()
        else:
            print("Pilihan Tidak Ada/Tidak ditemukan")
            show_data()
show_data()
