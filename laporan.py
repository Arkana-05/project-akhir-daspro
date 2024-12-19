# import modul
from tabulate import tabulate
#Mengimport letter untuk ukuran kertas pdf-nya
from reportlab.lib.pagesizes import letter 
#mengimport fungsi untuk memanipulasi dokumen pdf
from reportlab.pdfgen import canvas 
#mengimport fungsi untuk mmemberi warna pada tabel di pdf
from reportlab.lib import colors 
#mengimport fungsi untuk memanipulasi style table
from reportlab.platypus import Table , TableStyle

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

#Fungsi Membuat PDF
def create_pdf(data, total_keseluruhan, pdf_file):
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter
    # Menambahkan teks ke halaman
    c.drawString(210, 750, "PROGRAM PENGADAAN BARANG")
    c.drawString(235, 730, "PT DIGITAL IT PROGRAM")
    c.drawString(264, 710, "TAHUN 2024")
    
    # Menambahkan elemen grafis lainnya
    c.line(100, 700, 500, 700)  # Garis horizontal
    # Buat tabel di PDF
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Posisi tabel di PDF
    table.wrapOn(c, width, height)
    table_width, table_height = table.wrap(0, 0)
    x_position = (width - table_width) / 2
    y_position = height - table_height - 200  # Sesuaikan posisinya

    # Gambar tabel di canvas PDF
    table.drawOn(c, x_position, y_position)

    # Tambahkan total keseluruhan di bawah tabel
    c.drawString(x_position, y_position - 20, f"Total Keseluruhan: Rp.{total_keseluruhan:,.0f}")

    # Simpan PDF
    c.save()

# Fungsi untuk menampilkan data
def show_data(db, pdf_file):
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
        table_data = [headers] + result
        print(tabulate(result, headers=headers, tablefmt="pretty"))

        # Menjumlahkan total dari semua barang
        total_keseluruhan = sum(int(row[4]) for row in result)  # row[4] adalah kolom 'total' berdasarkan tabel yang ada di database
        
        # Menampilkan total keseluruhan di bawah tabel
        print(f"Total Keseluruhan: Rp.{total_keseluruhan:,.0f}")

        while(True):
            cetak_data = input("Ingin Mencetak Data? [Y/N] : ").upper()
            if cetak_data == 'Y':
                create_pdf(table_data, total_keseluruhan, pdf_file)
                print("Data Tercetak, terimakasih")
            elif cetak_data == 'N':
                print("Terimakasih")
            else:
                print("Warning!!! Masukkan dalam format [Y/N]")
                continue
            break

# Jalankan fungsi untuk menampilkan data


