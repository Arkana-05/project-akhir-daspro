# variabel untuk menampilkan = sebanyak 60
garis = ("=")*60

print(garis) #menampilkan isi dari variable garis
print("Selamat Datang".upper().center(60)) # upper() dapat mengubah teks menjadi kapital semua, dan center untuk mengubah teks menjadi di tengah
print("Admin PT RADAR IT".center(60))
print(garis) #menampilkan isi dari variable garis
print() #code untuk memberi jarak sebanyak 1 kali enter



# PROSES
while(True):
    # PROSES INPUT
    perintah = input("Apakah Anda ingin Login? [Y/T]: ").lower() 
    if  perintah == "y":
        import loginForm
        print(loginForm) # JIKA MEMILIH Y, MAKA AKAN OTOMATIS BERALIH PADA FILE LOGINFORM.PY
        break
    elif perintah == "t":
        print("Terimakasih")
        break
    else:
        print("WARNING !!! Input dengan Format [Y/T]")
        continue