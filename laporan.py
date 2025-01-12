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
#mengimport fungsi untuk memanipulasi font pdf
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import mysql.connector
import datetime

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
print("PT RADAR IT".center(60))
print("Tahun 2025".center(60))
print(garis) #menampilkan isi dari variable garis
print()



#Fungsi Membuat PDF
def create_pdf(data, total_keseluruhan, pdf_file):
    # Mendapatkan tanggal dan waktu saat ini
    current_datetime = datetime.datetime.now()
    # Mendapatkan tanggal hari ini
    current_date = current_datetime.date()
    # Mendapatkan hari dalam minggu (Senin = 0, Minggu = 6)
    current_day_of_week = current_datetime.weekday()
    # Konversi hari dalam bentuk teks (ex: 0 = Senin)
    days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    current_day_text = days[current_day_of_week]
    # Mendapatkan bulan saat ini
    current_month = current_datetime.month
    # Konversi bulan ke dalam bentuk teks
    months = [
        "Januari", "Februari", "Maret", "April",
        "Mei", "Juni", "Juli", "Agustus",
        "September", "Oktober", "November", "Desember"
    ]
    current_month_text = months[current_month - 1]

    current_year = current_datetime.year

    pdfmetrics.registerFont(TTFont('timesNewRomanBold', 'Times New Roman Bold.ttf'))
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter
    # Menambahkan teks ke halaman
    c.setFont("timesNewRomanBold", 12)  # Font dan ukuran teks
    c.drawString(230, 750, "LAPORAN DATA BARANG")
    c.drawString(265, 730, "PT RADAR IT")
    c.drawString(268, 710, "TAHUN 2025")
    
    # Menambahkan elemen grafis lainnya
    c.line(80, 700, 540, 700)  # Garis horizontal
    c.drawString(400,680, f"{current_day_text}, {str(current_date)[8:10]} {current_month_text} {current_year}")
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
    c.drawString(x_position, y_position - 20, f"Total Keseluruhan: Rp {total_keseluruhan:,.0f}".replace(",","."))

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

        # Format data untuk kolom Harga Satuan dan Total ke format Rupiah dengan pemisah titik
        formatted_result = [
            [
                row[0], 
                row[1], 
                row[2], 
                f"Rp {int(row[3]):,}".replace(",", "."),  # Format Harga Satuan
                f"Rp {int(row[4]):,}".replace(",", ".")   # Format Total
            ] 
            for row in result
            # memproses setiap elemen dalam result satu per satu,
        ]

        # Gabungkan header dengan data
        table_data = [headers] + formatted_result
        
        # Cetak tabel dengan format Rupiah
        print(tabulate(formatted_result, headers=headers, tablefmt="pretty"))

        # menjumlahkan semua nilai di kolom terakhir (kolom total) dari variable result
        total_keseluruhan = sum(int(column[4]) for column in result)  # column[4] adalah kolom 'total' berdasarkan tabel yang ada di database
        
        # Menampilkan total keseluruhan di bawah tabel
        print(f"Total Keseluruhan: Rp.{total_keseluruhan:,.0f}".replace(",", "."))

        while(True):
            cetak_data = input("Ingin Mencetak Data? [Y/T] : ").upper()
            if cetak_data == 'Y':
                create_pdf(table_data, total_keseluruhan, pdf_file)

                print("Data Tercetak, terimakasih")
                
            elif cetak_data == 'T':
                print("Terimakasih")
              
            else:
                print("Warning!!! Masukkan dalam format [Y/T]")
                continue
            while(True):
                perintah = input("Tampilkan Menu Utama [Y/T] : ").upper()
                if perintah == 'Y':
                    import menu
                    menu.show_menu()
                    break
                elif perintah == 'T':
                    print("Terimakasih")
                    exit()
                else:
                    print("Warning!!! Masukkan dalam format [Y/T]")
            continue

# Nama file PDF yang akan dibuat
pdf_file = "laporan_data_barang.pdf"

# Jalankan fungsi untuk menampilkan data
show_data(db, pdf_file)
