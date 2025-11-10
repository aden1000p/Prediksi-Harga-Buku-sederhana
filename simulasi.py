

daftar = {
    
}

buku = input("masukan judul buku: ")
penerbit = input("masukan penerbit: ")
jenis = input("kriteria buku: ")
daftar[buku] = {'penerbit':penerbit, 'jenis':jenis}



for i in daftar.values():
    print(i)