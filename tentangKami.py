# variabel untuk menampilkan = & - sebanyak 60
garis = ("=")*60
baris = ("-")*60

# code untuk menampilkan header
print() 
print("Program pengadaan barang".upper().center(60)) 
#menampilkan kata program ... dengan huruf kapital semua(upper) dan di setting ada di tengah dengan code center(60), angka 60 di samakan dengan banyaknya garis/baris di atas. 
print("PT DIGITAL IT PROGRAM".center(60))
print("Tahun 2024".center(60))
print(garis) #menampilkan isi dari variable garis
print()

print("Kelompok Daspro".center(60))
print()
print("Ketua    : Dias Havits / 1924")
print("Anggota  : Ramdhan / 1924")
print("         : Anggraini S / 1924")
print("         : Arka N / 19241186")
print("         : Muhammad Arya D.A / 1924")
print()

show = input("Tampilkan Data Team [Y/T] : ").lower()
if show == 'y':
    print("Nama\t: Dias H.")
    print("NIM\t: 1924")
    print("Prodi\t: Sistem Informasi")
    print("Kelas\t: 19.1B.13")
    print("Posisi\t: Ketua")
    print()
    print("Nama\t: Ramdhan")
    print("NIM\t: 1924")
    print("Prodi\t: Sistem Informasi")
    print("Kelas\t: 19.1B.13")
    print("Posisi\t: Anggota")
    print()
    print("Nama\t: Anggraini S.")
    print("NIM\t: 1924")
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
    print("NIM\t: 1924")
    print("Prodi\t: Sistem Informasi")
    print("Kelas\t: 19.1B.13")
    print("Posisi\t: Anggota")
    print()
    
    back = input("Kembali ke Menu [Y/T] : ").lower()
    if back == 'y':
        import menu
        menu.show_menu()
    else:
        print("Keluar dari program. Terimakasih😉")
        exit()
else:
    back = input("Kembali ke Menu [Y/T] : ").lower()
    if back == 'y':
        import menu
        menu.show_menu()
    else:
        print("Keluar dari program. Terimakasih😉")
        exit()