# soal 1
npm = float(input("Masukan npm : "))

print(npm)
angka1 = "="
if angka1 == "=":
    hasil = npm * (1 + 10 / 31 ) ** 5 + 2
    print(f"hasilnya adalah {hasil}")

#soal 2
nilai_1 = float(input("Inputkan Nilai Pertama: "))
nilai_2 = float(input("Inputkan Nilai Kedua: "))
operator = input("Inputkan Opertor (*) ")

if operator == "*":
    hasil =  nilai_1 * nilai_2
    print(f"Hasil {nilai_1} * {nilai_2} = {hasil}")


print("="*32)

# soal 3
celcius = float (input ("masukan suhu dalam celcius: "))
print("suhu adalah = ", celcius, "celcius")

f = (9/5* celcius ) + 32
print("suhu dalam farenhet adalah = ", f, "farenhet")



