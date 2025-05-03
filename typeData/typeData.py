#type data adalah macam-macam data pada python yang bisa kita gunakan

# 1. Integer (int): type data untuk bilangan bulat, baik postif maupun negatif, termasuk nol.
data_int = 1 
print ("Data:", data_int)
print ("Tipe:", type(data_int))

# 2. Float (float): tipe data untuk bilangan desimal/pecahan
data_float = 2.5
print ("Data:", data_float)
print ("Tipe:", type(data_float))

# 3. String (str): tipe data untuk teks/kumpulan karakter, baik huruf, angka, maupun karakter.
# String diapit oleh tanda petik satu (' ') atau tanda petik dua (" ").
data_str = "Hello World!"
print ("Data:", data_str)
print ("Tipe:", type(data_str))

# 4. Booloean (bool): tipe data untuk nilai binner (True/False)
data_bool = True
print ("Data:", data_bool)
print ("Tipe:", type(data_bool))

# 5. Kompleks (complex): tipe data untuk bilangan kompleks, terdiri dari bilangan real dan imajiner
# ditulis dengna format: a + bj, a = bilangan real, b = bilangan imajiner, j = akar dari -1
data_complex = (1 + 2j)
print ("Data:", data_complex)
print ("Tipe:", type(data_complex))

# tipe data bahasa C
from ctypes import c_int, c_float, c_double, c_char, c_bool, c_wchar, c_wchar_p, c_void_p #import library

data_double = 1.5869893
print ("Data:", data_double)
print ("Tipe:", c_double(data_double)) #c_double untuk menampilkan tipe data double
