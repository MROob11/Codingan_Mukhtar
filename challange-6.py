def hitung_persegi_panjang(panjang, lebar):
    return panjang * lebar

def hitung_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def hitungan():
    pilihan = input("Masukkan pilihan (persegi panjang / segitiga): ")
    
    if pilihan == "persegi panjang":
        panjang = int(input("Masukkan panjang persegi panjang: "))
        lebar = int(input("Masukkan lebar persegi panjang: "))
        luas = hitung_persegi_panjang(panjang, lebar)
        print(f"Luas persegi panjang adalah: {luas}")

    elif pilihan == "segitiga":
        alas = int(input("Masukkan alas segitiga: "))
        tinggi = int(input("Masukkan tinggi segitiga: "))
        luas = hitung_segitiga(alas, tinggi)
        print(f"Luas segitiga adalah: {luas}")

    else:
        print("Harap masukkan pilihan 'persegi panjang' atau 'segitiga'.")

hitungan()