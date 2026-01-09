from data import Mahasiswa
from process import ProsesNilai

class Tampilan:
    def input_data(self):
        nama = input("Masukkan Nama Mahasiswa: ")
        nim = input("Masukkan NIM: ")

        nilai = []
        for i in range(3):
            while True:
                try:
                    n = int(input(f"Masukkan Nilai ke-{i+1}: "))
                    if n < 0 or n > 100:
                        raise ValueError
                    nilai.append(n)
                    break
                except ValueError:
                    print("Input harus angka 0 - 100!")

        return Mahasiswa(nama, nim, nilai)

    def tampilkan_hasil(self, mahasiswa):
        proses = ProsesNilai()
        rata = proses.hitung_rata_rata(mahasiswa.nilai)

        print("\n===== HASIL =====")
        print("Nama       :", mahasiswa.nama)
        print("NIM        :", mahasiswa.nim)
        print("Nilai      :", mahasiswa.nilai)
        print("Rata-rata  :", rata)
