# latihan perulangan segitiga

sisi = int(input("Masukan panjang sisi = "))

# 1. menggunkaan for

# dummy variable
print("awal dari for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("akhir dari for")
# 2. menggunakan while

print("awal while")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("akhir dari while")

# 4. hanya ganjil saja

print("awal while")
count = 1
spasi = int(sisi/2)
while True:
    # print jika ganjil
    if (count % 2):
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjl
        count += 1
        continue

    # akan break jika count melebehi sisi
    if count > sisi:
        break

print("akhir dari while")

# 5. hanya ganjil saja

print("awal while")
count = 1
while True:
    # print jika ganjil
    if (count % 2):
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika ganjl
        count += 1
        continue

    # akan break jika count melebehi sisi
    if count > sisi:
        break


# 6. ketupat

print("awal tugas")
panjang = 1
count = 1
while True:
    # print jika ganjil
    if (count < sisi):
        print((panjang*"+").center(sisi+1))
        count += 2
        panjang += 2
    else:
        # akan kembali ke atas jika ganjl
        print((panjang*"+").center(sisi+1))
        panjang -= 2
        

    # akan break jika count melebehi sisi
    if panjang < 1:
        break

print("akhir dari tugas")