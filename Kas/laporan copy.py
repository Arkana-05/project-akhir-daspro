from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tabulate import tabulate
# import modul
import mysql.connector

# Code untuk dapat terkoneksi ke database MySQL
db = mysql.connector.connect(
    host = "localhost",      # host database, biasanya pakai localhost
    user = "root",           # username MySQL, user biasaya root
    password = "",           # password MySQL, password disesuaikan, kalo mac biasanya pw sama dengan user
    database = "python_project_uas"  # Nama database
)

# Fungsi untuk membuat file PDF
def generate_pdf(data, headers):
    try:
        # Buat file PDF
        pdf = canvas.Canvas("output.pdf", pagesize=letter)
        pdf.setTitle("Data Barang")
        
        # Tambahkan judul ke PDF
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(50, 750, "Data Barang")
        pdf.setFont("Helvetica", 10)
        
        # Posisi awal di halaman
        x = 50
        y = 730

        # Tambahkan header
        header_text = f"{headers[0]:<10} {headers[1]:<20} {headers[2]:<10} {headers[3]:<15} {headers[4]:<10}"
        pdf.drawString(x, y, header_text)
        pdf.line(x, y - 2, 550, y - 2)  # Garis bawah header
        y -= 20

        # Tambahkan data
        for row in data:
            row_text = f"{row[0]:<10} {row[1]:<20} {row[2]:<10} {row[3]:<15} {row[4]:<10}"
            pdf.drawString(x, y, row_text)
            y -= 15
            if y < 50:  # Jika data melebihi halaman, buat halaman baru
                pdf.showPage()
                pdf.setFont("Helvetica", 10)
                y = 750

        # Simpan PDF
        pdf.save()
        print("PDF berhasil disimpan sebagai 'output.pdf'.")

    except Exception as e:
        print(f"Terjadi error saat menyimpan PDF: {e}")

# Fungsi untuk menampilkan data
def show_data(db):
    cursor = db.cursor()
    # MENGAMBIL SEMUA DATA YANG ADA DALAM TABEL DATA_BARANG
    cursor.execute("SELECT kode, nama, qty, harga, total FROM data_barang")
    result = cursor.fetchall()  # Mengambil semua data dari query

    if cursor.rowcount == 0:  # Jika tidak ada data dalam tabel
        print("Tidak Ada Data yang Ditampilkan")
    else:
        print("Data Barang".center(60))
        headers = ["Kode", "Nama Barang", "Quantity", "Harga Satuan", "Total"]
        print(tabulate(result, headers=headers, tablefmt="pretty"))
        generate_pdf(result, headers)

# Jalankan fungsi untuk menampilkan data
show_data(db)
