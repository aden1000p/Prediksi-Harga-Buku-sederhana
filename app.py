import time as ti
import numpy as np
import os
from model.project import model

daftar_isi = {}

os.system('cls')

def baris(n):
    print("=" * n)

def tampilan_utama():
    global daftar_isi
    for i in range(30):
        baris(30)
        if i == 3:
            while True:
                judul = input("masukan Judul Nama: ")
                kategori = input("kategori: ")
                hari_rilis = int(input("masukan hari rilis: "))
                bulan_rilis = int(input("masukan bulan rilis: "))
                tahun_rilis = int(input("masukan tahun rilis: "))
                lebar = int(input("masukan lebar: "))
                panjang = int(input("masukan tinggi: "))
                lembar = int(input("masukan lembar tersedia: "))
                
                rilis = f'{hari_rilis}/{bulan_rilis}/{tahun_rilis}'
                ukuran = panjang * lebar
                
                X_new = np.array([ukuran, lembar]).reshape(1, -1)
                y_pred = model.predict(X_new)
                
                daftar_isi[judul] = {'kategori': kategori, 'terbit': rilis, 'ukuran':ukuran, 'lembar':lembar, 'harga':f'Rp {int(y_pred)} Ribu'}
                
                baris(200)
                print("\t\tToko Buku Sederhana")
                baris(200)
                print(f"{"Nama":^20} {"kategori":^20} {"terbit":^20} {"ukuran":^20} {"lembar":^20} {"Harga":^20}")
                for nama, data in zip(daftar_isi.keys(), daftar_isi.values()):
                    judul = nama
                    kategori = data['kategori']
                    terbit = data['terbit']
                    ukuran = data['ukuran']
                    lembar = data['lembar']
                    harga = data['harga']
                    
                    baris(200)
                    print(f"{nama:^20} {kategori:^20} {terbit:^20} {ukuran:^20} {lembar:^20} {harga:^20}")
                    baris(200)
                
                is_done = input("apakah sudah cukup? ")
                
                if is_done == 'y':
                    break

if __name__ == "__main__":
    tampilan_utama()
    print("program berakhir")