import getpass
# variabel untuk menampilkan = & - sebanyak 60
garis = ("=")*60
baris = ("-")*60

def header():
    print() #code untuk memberi jarak sebanyak 1 kali enter
    print("Program pengadaan barang".upper().center(60)) # upper() dapat mengubah teks menjadi kapital semua, dan center untuk mengubah teks menjadi di tengah
    print("PT RADAR IT".center(60))

    print(garis) #menampilkan isi dari variable garis
    print()

# PROSES INPUT USERNAME DAN PASSWORD

while True:
    header()
    user = input("\t User \t\t: ").lower()
    password = getpass.getpass("\t Password \t: ").lower()
    
    if user == "master" and password == "radar":
        import menu
        print(menu.show_menu())  # JIKA USER DAN PW SUDAH BENAR, MAKA AKAN OTOMATIS BERALIH PADA FILE MENU.PY DAN LANGSUNG MENJALANKAN FUNGSI SHOW_MENU()
    else:
        print('\n')
        print("Maaf Username atau Password Salah, Silahkan Coba Lagi")
        print('\n')
        while(True):
            continueLogin = input("Apakah Anda Ingin Mencoba Lagi? [Y/T]: ").lower()
            if continueLogin == "y":
                break
            elif continueLogin == "t":
                print("Terimakasih")
                break
            else:
                print("WARNING !!! Input dengan Format [Y/T]")
                continue
        if continueLogin == "t":
            break


# LOGIKA LOGIN
# if user == "Master" or user == "master" and password == "ptdigi" or password == "PTDIGI":
#     import menu
#     print(menu.show_menu())  # JIKA USER DAN PW SUDAH BENAR, MAKA AKAN OTOMATIS BERALIH PADA FILE MENU.PY DAN LANGSUNG MENJALANKAN FUNGSI SHOW_MENU()
# else:
#     print("Maaf Username atau Password Salah, Silahkan Coba Lagi")
