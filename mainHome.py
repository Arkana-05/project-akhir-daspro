# variabel untuk menampilkan = sebanyak 60
garis = ("=")*60

print(garis) #menampilkan isi dari variable garis
print("Selamat Datang".upper().center(60)) # upper() dapat mengubah teks menjadi kapital semua, dan center untuk mengubah teks menjadi di tengah
<<<<<<< HEAD
print("Admin PT RADAR IT PROGRAM".center(60))
=======
print("Admin PT RADAR IT".center(60))
>>>>>>> ba10bedb7c79166d3c0fe1e2e6404ced67ad36f9
print(garis) #menampilkan isi dari variable garis
print() #code untuk memberi jarak sebanyak 1 kali enter

# PROSES INPUT
perintah = input("Apakah Anda ingin Login? [Y/T]: ")

# PROSES
if perintah == "Y" or perintah == "y":
    import loginForm
    print(loginForm) # JIKA MEMILIH Y, MAKA AKAN OTOMATIS BERALIH PADA FILE LOGINFORM.PY
else:
    print("Terimakasih")
