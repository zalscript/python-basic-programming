# Variabel adalah tempat untuk menyimpan nilai/data

# contoh:
nama = "John Doe" # 'nama' merupakan variabel yang menyimpan string "John Doe"   # 'nama' --> variabel
umur = 15 # 'umur' merupakan variabel yang menyimpan nilai 15                    # '=' --> operator penugasan/assignment            
                                                                                 # 'John Doe' --> nilai/data

# pemanggilan variabel
print(nama) # memanggil variabel 'nama' untuk menampilkan nilainya
print(umur) # memanggil variabel 'umur' untuk menampilkan nilainya

# aturan/cara penamaan variabel
# 1. tidak boleh diawali dengan angka
# 2. tidak boleh menggunakan karakter khusus seperti @, #, $, %, ^, &, *, (, ), -, +, =, {, }, [, ], ;, :, ", ', <, >, ?, /, \, |, `, ~
# 3. tidak boleh menggunakan spasi
# 4. tidak boleh menggunakan kata kunci yang sudah ada di python seperti if, else, for, while, def, class, import, from, as, try, except, finally, with, lambda, return, yield, break, continue, pass, raise, assert, global, nonlocal, del, in, is, and, or, not
nama_lengkap = "John Doe" # menggunakan underscore (_) sebagai pengganti spasi
umurSekarang = "lorem ipsum" # menggunakan huruf besar untuk memisahkan kata

# pemanggilan kedua dari variabel
print("nama:", nama_lengkap) 
nama_lengkap = "Richard Roe"  # mengubah nilai dari variabel 'nama_lengkap' menjadi "Richard Roe"
print("nama:", nama_lengkap) 

# indirect assignment
namaProgrammer = nama_lengkap # 'namaProgrammer' merupakan variabel yang menyimpan nilai/data dari variabel 'nama_lengkap'
print("Nama Programmer:", namaProgrammer) # memanggil variabel 'NamaProgrammer' untuk menampilkan nilainya