rekap_nilai = {
    'Basic English for Academic Purposes': {
        'Nama Dosen': 'Dr. Dyah Mukaromah, S.Pd., M.Pd.,',
        'NIK': '12345678',
        'Nilai': [80, 88, 63, 94, 92, 73]
    },
    'Logika Informatika': {
        'Nama Dosen': 'Wahyu Sri Utami, S.Si., M.Sc.',
        'NIK': '87654321',
        'Nilai': [81, 70, 73, 84, 20, 80]
    },
    'Pengantar Teknologi Informasi': {
        'Nama Dosen': 'Anna Dina Kalifia,. S.Kom., M.Cs',
        'NIK': '11223344',
        'Nilai': [78, 82, 85, 79, 44, 88]
    },
    'PENGEMBANGAN KEPRIBADIAN': {
        'Nama Dosen': 'Antonius Bangkit Wirasmoyo, MA',
        'NIK': '44332211',
        'Nilai': [75, 80, 82, 42, 88, 90]
    },
    'Pengembangan Web dan Mobile': {
        'Nama Dosen': 'Murti Retnowo, S.KOM., M.CS,',
        'NIK': '99887766',
        'Nilai': [88, 90, 49, 85, 80, 87]
    }
}

def hitung_rata_rata_nilai():
    rata_rata = {}
    for mata_kuliah, data in rekap_nilai.items():
        total = 0
        count = 0
        for nilai in data['Nilai']:
            total += nilai
            count += 1
        if count > 0:
            rata_rata[mata_kuliah] = total / count
    return rata_rata


def input_nilai_mata_kuliah(mata_kuliah, nilai_baru):
    if mata_kuliah in rekap_nilai:
        count = 0
        for _ in rekap_nilai[mata_kuliah]['Nilai']:
            count += 1
        rekap_nilai[mata_kuliah]['Nilai'][count:] = [nilai_baru]
        print(f"Nilai {nilai_baru} berhasil ditambahkan pada mata kuliah {mata_kuliah}.")
    else:
        print(f"Mata kuliah '{mata_kuliah}' tidak ditemukan.")


print("=" * 128)
print("Data awal rekap nilai:")
print(rekap_nilai)
print("=" * 128)
print("\nRata-rata nilai per mata kuliah:")
print(hitung_rata_rata_nilai())
input_nilai_mata_kuliah('Pengembangan Web dan Mobile', 95)
print("=" * 128)
print("\nData rekap nilai setelah penambahan:")
print(rekap_nilai)