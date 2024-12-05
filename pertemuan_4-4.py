# Kalkulator sederhana

print("="*32)
print("-"*5,"Kalkulator Sederhana","="*5)
print("="*32)

print("\n")
nilai_1 = float(input("Inputkan Nilai Pertama: "))
nilai_2 = float(input("Inputkan Nilai Kedua: "))
operator = input("Inputkan Opertor (+, -, *, /, **, %, //): ")

# Penjumlahan
if operator == "+":
    hasil =  nilai_1 + nilai_2
    print(f"Hasil {nilai_1} + {nilai_2} = {hasil}")
# pengurangan
elif operator == "-":
    hasil =  nilai_1 + nilai_2
    print(f"Hasil {nilai_1} - {nilai_2} = {hasil}")
# perkalian
elif operator == "*":
    hasil =  nilai_1 + nilai_2
    print(f"Hasil {nilai_1} * {nilai_2} = {hasil}")
# pembagian
elif operator == "/":
    hasil =  nilai_1 + nilai_2
    print(f"Hasil {nilai_1} / {nilai_2} = {hasil}")
# pangkat
elif operator == "**":
    hasil =  nilai_1 + nilai_2
    print(f"Hasil {nilai_1} ** {nilai_2} = {hasil}")
# modulus
elif operator == "%":
    hasil =  nilai_1 + nilai_2
    print(f"Hasil {nilai_1} % {nilai_2} = {hasil}")
# floor div
elif operator == "//":
    hasil =  nilai_1 + nilai_2
    print(f"Hasil {nilai_1} // {nilai_2} = {hasil}")
else:
    print("Operator tidak sesuai")

print("="*32)



# String procesing -> python (peajari sendiri)