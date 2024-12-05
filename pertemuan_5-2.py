# break, continue, pass
# break => mengehentikan looping
# continue => untuk melanjutkan break

awal = 0
batas = 10
while awal <= batas:
    if awal == 5:
        continue
        print("World")

    print(f"hello {awal}")
    awal += 1
