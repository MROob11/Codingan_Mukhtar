# Program Konversi Nilai
#? A = niali => 81
#? B = 61 >= nilai >= 80
#? C = 41 >= nilai >= 60
#? D = 21 >= nilai >= 40
#? E = nilai < 21





nilai = int(input("masukan nilai : "))

if nilai >= 81:
    print("nilai = A")
elif nilai >= 61:
    print("nilai = B")
elif nilai >= 41:
    print("nilai = C")
elif nilai >= 21:
    print("nilai = D")
else:
    print("nilai = E")