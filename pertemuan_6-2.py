# buat program menghitung luas & keliling persegi panjang
def hedear():
    print("="*5, "PROGRAM MENGHITUNG LUAS & KELILING", "="*5)
    print("="*14, "PERSEGI PANJANG: ", "="*14)

def input_user():
    panjang = int(input("Inputkan panjang : "))
    lebar = int(input("Inputkan Lebar : "))
    return panjang, lebar

def hitung_luas(panjang, lebar):
    return panjang * lebar

def hitung_keliling(panjang, lebar):
    return 2 * (panjang + lebar)

def tampilkan_output(panjang, lebar, luas, keliling):
    print(f"Panjang\t\t : {panjang}")
    print(f"lebar\t\t : {lebar}")
    print(f"luas\t\t : {luas}")
    print(f"keliling\t : {keliling}")
    print("-"*44)


# buat program berulang untuk menghitung luas & keliling
hedear()
while True:
    panjang, lebar = input_user()
    luas = hitung_luas(panjang, lebar)
    keliling = hitung_keliling(panjang, lebar)
    tampilkan_output(panjang, lebar, luas, keliling)
    is_break = input("lanjutkan program (y/n): ")
    if is_break == "n":
        break