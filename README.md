# PratikumUAS-Semester1-

✨📘 **Project UAS Bahasa Pemrograman** 📘✨

Program ini dibuat untuk memenuhi tugas **Ujian Akhir Semester (UAS)** pada mata kuliah **Bahasa Pemrograman** 💻📚.
Program yang dibuat merupakan program sederhana menggunakan bahasa **Python** dengan menerapkan konsep **Object Oriented Programming (OOP)** dan **modular programming** 🧠✨.

Dalam program ini, struktur kode dibagi menjadi beberapa bagian agar lebih rapi dan mudah dipahami 🌱.
Setiap bagian memiliki tugas masing-masing, yaitu untuk menyimpan data, memproses data, serta menampilkan hasil kepada pengguna 👩‍💻👨‍💻.

Program akan meminta pengguna untuk memasukkan **nama mahasiswa**, **NIM**, dan **nilai** 📝.
Data yang dimasukkan kemudian diproses untuk menghitung **rata-rata nilai**, lalu hasilnya ditampilkan ke layar 📊✨.

Agar program tidak mudah mengalami error, ditambahkan **validasi input** menggunakan konsep **exception handling** ⚠️.
Validasi ini berguna untuk mencegah kesalahan input, seperti memasukkan huruf pada saat program meminta angka 🔢❌.

Secara keseluruhan, program ini dibuat untuk melatih pemahaman mengenai:

* konsep OOP 🧩
* modular programming 📂
* exception handling 🚨
* serta penulisan program Python yang rapi dan terstruktur ✨

💾 **Berikut adalah kode program yang digunakan:**

🌸 **File: `data.py`**
File ini digunakan untuk menyimpan data mahasiswa dalam bentuk class.

```python
class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai
```

⚙️ **File: `process.py`**
File ini berisi proses perhitungan rata-rata nilai mahasiswa.

```python
class ProsesNilai:
    def hitung_rata_rata(self, nilai):
        return sum(nilai) / len(nilai)
```

🖥️ **File: `view.py`**
File ini berfungsi untuk menerima input dari pengguna dan menampilkan hasil program.

```python
from data import Mahasiswa
from process import ProsesNilai

class Tampilan:
    def input_data(self):
        nama = input("Masukkan Nama: ")
        nim = input("Masukkan NIM: ")

        nilai = []
        for i in range(3):
            while True:
                try:
                    n = int(input(f"Masukkan Nilai ke-{i+1}: "))
                    nilai.append(n)
                    break
                except:
                    print("Input harus berupa angka!")

        return Mahasiswa(nama, nim, nilai)

    def tampilkan_hasil(self, mahasiswa):
        proses = ProsesNilai()
        rata = proses.hitung_rata_rata(mahasiswa.nilai)

        print("Nama :", mahasiswa.nama)
        print("NIM :", mahasiswa.nim)
        print("Nilai :", mahasiswa.nilai)
        print("Rata-rata :", rata)
```

🚀 **File: `main.py`**
File ini merupakan file utama yang digunakan untuk menjalankan seluruh program.

```python
from view import Tampilan

app = Tampilan()
data = app.input_data()
app.tampilkan_hasil(data)
```

🌷 **Penutup**
Dengan adanya program ini, diharapkan mahasiswa dapat memahami penerapan konsep OOP, modular programming, serta exception handling dalam pembuatan program Python sederhana. Program ini juga menjadi latihan awal dalam membangun aplikasi yang lebih terstruktur dan aman dari kesalahan input ✨💡.

👩‍💻 **Penyusun:**
Nabila Fawwaz Nurliah

(312510255)

TI.25.A.2

Teknik Informatika

2026 🌸

🎥 Dokumentasi & Demo

📺 Video Penjelasan & Demo Program (YouTube)
```
👉 https://youtu.be/FVJzhbbMjuU?si=YnckVFTjkg_8wdFL
```
