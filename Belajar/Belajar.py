def hitung_luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def main():
    print("Pilih bentuk geometri untuk menghitung luas:")
    print("1. Persegi Panjang")
    print("2. Segitiga")
    
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == "1":
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        luas = hitung_luas_persegi_panjang(panjang, lebar)
        print("Luas persegi panjang adalah:", luas)
    elif pilihan == "2":
        alas = float(input("Masukkan alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = hitung_luas_segitiga(alas, tinggi)
        print("Luas segitiga adalah:", luas)
    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

main()