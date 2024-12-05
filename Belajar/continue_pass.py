# continue, pass

# pass -> dia berfungsi sebagai dummi, tidak akan di eksekusi

angka  = 0

while angka < 5:
    angka += 1

    if angka == 3:
        # print("wawwwww!")
        pass # ini tidak akan dieksekusi

    print(angka)

# continue

angka = 0

print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # aksi 1

    if angka == 3:
        print("nice!")
        continue # akan membuat loop meloncat ke step selanjutnya

    print("hello!!") # aksi 2

print("finish!")