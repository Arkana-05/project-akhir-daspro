# variabel untuk menampilkan = & - sebanyak 60
garis = ("=")*60
baris = ("-")*60

print() #code untuk memberi jarak sebanyak 1 kali enter
print("Program pengadaan barang".upper().center(60)) # upper() dapat mengubah teks menjadi kapital semua, dan center untuk mengubah teks menjadi di tengah
print("Program Kas Sweety Slice & PITAK".center(60))

print(garis) #menampilkan isi dari variable garis
print()

# PROSES INPUT USERNAME DAN PASSWORD
user = input("\t User \t\t: ").lower()
password = input("\t Password \t: ").lower()

# LOGIKA LOGIN
if user == "master" and password == "sp":
    import menuKas
    menuKas.show_menu()  # JIKA USER DAN PW SUDAH BENAR, MAKA AKAN OTOMATIS BERALIH PADA FILE MENU.PY DAN LANGSUNG MENJALANKAN FUNGSI SHOW_MENU()
else:
    print("Maaf Username atau Password Salah, Silahkan Coba Lagi")