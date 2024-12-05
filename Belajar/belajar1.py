# Membuat struktur data awal untuk matkul
rekap_nilai = {}

# Fungsi untuk menambah data mata kuliah dan nilai
def tambah_mata_kuliah():
    print("=" * 100)
    matkul = input("Masukkan matkul : ")
    print("=" * 100)
    nama_dosen = input("Masukkan nama dosen : ")
    print("=" * 100)
    nik = input("Masukkan NIK dosen : ")
    print("=" * 100)

    # Menambahkan data mata kuliah
    rekap_nilai[matkul] = {
        'Nama Dosen': nama_dosen,
        'NIK': nik,
        'Nilai': []
    }

def input_nilai_mata_kuliah():
    print("=" * 100)
    matkul = input("Masukkan matkul untuk menambahkan nilai : ")
    
    # Pengecekan apakah mata kuliah ada
    if matkul in rekap_nilai:
        nilai_baru = int(input("Masukkan nilai baru mahasiswa : "))
        
        # Tambahkan nilai ke daftar tanpa fungsi bawaan
        i = 0
        new_nilai = []
        while i < len(rekap_nilai[matkul]['Nilai']):
            new_nilai += [rekap_nilai[matkul]['Nilai'][i]]
            i += 1
        new_nilai += [nilai_baru]
        rekap_nilai[matkul]['Nilai'] = new_nilai
        print("=" * 100)
        print(f"Nilai {nilai_baru} berhasil ditambahkan ke matkul {matkul}.")
    else:
        print("Matkul tidak ditemukan.")

# Fungsi untuk menghitung rata-rata nilai setiap mata kuliah
def hitung_rata_rata_nilai():
    rata_rata_nilai = {}
    for matkul, data in rekap_nilai.items():
        total = 0
        count = 0
        i = 0
        while i < len(data['Nilai']):
            total += data['Nilai'][i]  # Penjumlahan manual
            count += 1  # Hitung banyaknya elemen secara manual
            i += 1
        rata_rata_nilai[matkul] = total / count if count != 0 else 0
    return rata_rata_nilai

# Main program
print("Selamat datang di program rekap nilai matkul ini!")
running = True
while running:
    print("Menu:")
    print("1. Tambah Mata Kuliah")
    print("2. Input Nilai Mata Kuliah")
    print("3. Hitung Rata-rata Nilai")
    print("4. Tampilkan Data Mata Kuliah")
    print("5. Keluar")
    print("=" * 100)
    pilihan = input("Pilih menu (1 sampai 5): ")

    
    if pilihan == '1':
        tambah_mata_kuliah()
    elif pilihan == '2':
        input_nilai_mata_kuliah()
    elif pilihan == '3':
        print("\nrata-rata Nilai:")
        rata_rata = hitung_rata_rata_nilai()
        for matkul, rata in rata_rata.items():
            print(f"{matkul}: {rata}")
    elif pilihan == '4':
        print("\ndata Mata Kuliah:")
        for matkul, data in rekap_nilai.items():
            print(f"MatKul: {matkul}")
            print(f"Nama Dosen: {data['Nama Dosen']}")
            print(f"NIK: {data['NIK']}")
            print(f"Nilai: {data['Nilai']}")
    elif pilihan == '5':
        print("Terima kasih telah menggunakan program saya!")
        running = False
    else:
        print("Pilihan tidak valid. Silakan coba kembali.")